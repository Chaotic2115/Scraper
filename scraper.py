import requests
import bs4
import pandas as pd
import sys


def ziskej_soup(url):
    """
    Funkce pro získání soup ze zadaného url.
    """
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    return soup


def ziskej_df(url):
    """
    Funkce vrací DataFrame ze zadaného url, pokud url obsahuje tabulku.
    """
    df = pd.read_html(url, encoding="utf-8", header=1)
    return df


def ziskej_url(url):
    """
    Funkce pro získání listu odkazů na příslušné obce v okresu.
    """
    tabulka = ziskej_soup(url)
    ele = [a_elem["href"] for a_elem in tabulka.select("table a")]
    list_odkazu = []
    for i in ele[::2]:
        list_odkazu.append(i)
    return list_odkazu


def obce(url):
    """
    Funkce vrací DataFrame s číslem a jménem obce v celém okresu.
    """
    obce = ziskej_df(url)
    df_obce = pd.concat(obce)
    df_obce = df_obce[df_obce.název != "-"]
    return df_obce[["číslo", "název"]].reset_index().drop("index", axis=1)

def ziskej_data_pro_obce(url):
    """
    Funkce vrací DataFrame s daty o volbách v každé obci v okresu.
    """
    list_odkazu = ziskej_url(url)
    list_df = []
    for odkaz in list_odkazu:
        spojene_url = "https://volby.cz/pls/ps2017nss/" + odkaz
        df1 = ziskej_df(spojene_url)[0][["Voličiv seznamu", "Vydanéobálky", "Platnéhlasy"]]
        df1 = df1.transpose().rename(columns={0: "celkem"})
        df2 = ziskej_df(spojene_url)[1][["název", "celkem"]].set_index("název")
        df3 = ziskej_df(spojene_url)[2][["název", "celkem"]].set_index("název")
        df_s = df1.append(df2).append(df3).transpose()
        list_df.append(df_s)
    df_data_obci = pd.concat(list_df)
    return df_data_obci.reset_index().drop("index", axis=1)


def ulozeni(url, jmeno_souboru):
    """
    Funkce spojí dvě získané DataFrame a uloží výsledek do zadaného souboru.
    """
    print("\nStahuji data z URL: ", url)
    print("\nUkládám do souboru: ", jmeno_souboru)
    sys.stdout = open(f"{jmeno_souboru}", "w", encoding="cp1250")
    df1 = obce(url)
    df2 = ziskej_data_pro_obce(url)
    vysledna_df = df1.join(df2)
    print(vysledna_df.to_csv(sep=";", index=False, line_terminator="\n"))
    sys.stdout.close()
    

def main():
    try:
        url = sys.argv[1]
        jmeno_souboru = sys.argv[2]
        ulozeni(url, jmeno_souboru)
        sys.exit("\nStahování dokončeno!")
    except IndexError:
        print("\nNezadal jsi správné argumenty!")
        sys.exit()
    except OSError:
        print("\nZadal jsi argumenty ve špatném pořadí, nebo už máš otevřený výsledný soubor!")
        sys.exit()

main()