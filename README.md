# Scraper
Finální projekt na Engeto Python Academy.

<h2>Popis projektu</h2>
Tento scraper slouží k extrakci výsledků parlamentních voleb v roce 2017. 

Odkaz na [stránky](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

Z daného odkazu je možnost vybrat jakýkoliv územní celek. Stačí u kteréhokoliv celku zvolit X u výběr obce a daný odkaz použít pro scraper.

<h2>Instalace knihoven</h2>
Pro správné fungování scriptu je potřeba vytvořit nové virtuální prostředí. Knihovny se nainstalují pomocí příkazu:

```pip install -r requirements.txt```

<h2>Spuštění scriptu</h2>
Script je napsán v Python3.9 a spuštění scraper.py v příkazovém řádku vyžaduje dva povinné argumenty.

```python scraper.py <url> <jmeno_souboru.csv>```

<h2>Ukázka projektu</h2>

Ukázka spuštění pro okres Brno-Venkov.
 - první argument ```"https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203"```
 - druhý argument ```"vysledky_brno_venkov.csv"```

```python scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203" "vysledky_brno_venkov.csv"```

Ukázka průběhu

```
Stahuji data z URL:  https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203

Ukládám do souboru:  vysledky_brno_venkov.csv

Stahování dokončeno!
```

Ukázka části výstupu

```
číslo,název,Voličiv seznamu,Vydanéobálky,Platnéhlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,ROZUMNÍ-stop migraci,diktát.EU,Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů,Národ Sobě
582794,Babice nad Svitavou,925,660,655,109,1,2,43,0,53,31,7,3,10,0,0,93,0,39,129,0,3,69,0,2,1,1,58,1,0,
582808,Babice u Rosic,553,353,351,32,0,0,18,1,27,30,5,1,6,0,2,37,0,13,93,0,1,25,5,4,1,1,49,0,0,
581321,Běleč,160,131,130,13,0,0,25,0,8,14,0,1,0,0,0,11,1,1,30,0,0,14,0,0,0,0,12,0,0,
582824,Bílovice nad Svitavou,2676,2018,2004,316,0,2,103,0,257,78,28,6,44,2,0,205,2,147,432,2,6,186,0,16,0,1,170,1,0,
582832,Biskoupky,145,86,85,6,0,0,11,0,1,17,1,0,1,0,0,5,0,7,22,0,0,4,0,0,0,2,7,1,0,
582841,Blažovice,924,725,724,64,0,0,54,0,49,44,12,2,7,3,1,53,1,34,133,0,1,193,1,2,0,0,70,0,0,
582859,Blučina,1749,1099,1091,126,2,0,62,2,42,52,15,11,20,0,1,108,0,23,326,5,1,100,1,8,7,2,174,2,1,
```

