import json

termek = ["Sertéskaraj", "Gouda sajt", "Dobozos sajt", "Csirkemell filé", "Mirelit Pizza", "Vaj", "Edámi sajt", "Szőlő", "Paradicsom", "Szalámi", "Rizs", "Banán", "Zöldségmix", "Cola", "Hagyma", "Kenyér", "Narancs", "Alma", "Napraforgóolaj", "Spaghetti tészta", "Teljes tej", "Joghurt", "Almalé", "Burgonya", "Babkonzerv", "Cukor", "WC-papír", "Búzaliszt", "Friss tojás"]
egyseg = ["kg", "450 g", "400 g", "kg", "db", "250 g", "200 g", "1 kg", "1 kg", "100 g", "1 kg", "1 kg", "1 kg", "2l", "1 kg", "1 kg", "1 kg", "1 kg", "1 l", "500 g", "1 l", "500 ml", "1 l", "1 kg", "240 g", "1 kg", "tekercs", "1 kg", "db"]

# 1. feladat
# ▪ Kérje be a felhasználótól egy keresett termék nevét!
# ▪ Ellenőrizze, hogy az megtalálható-e a termékek között!
# ▪     Ha igen, akkor állapítsa meg az indexét és írja ki a kiszerelés egységét!
# ▪     Ha nem, akkor a parancssoron a „Nincs ilyen termék” üzenet jelenjen meg!

december = [ 2550, 1602, 1140, 1620, 1320, 682, 750, 1700, 1000, 693, 651, 686, 805, 702, 600, 582, 798, 648, 522, 605, 550, 567, 286, 350, 351, 250, 154, 135, 50 ]
november = [ 2400, 1800, 1500, 1500, 1500, 1100, 1000, 1000, 1000, 770, 700, 700, 700, 600, 600, 600, 600, 600, 580, 550, 440, 540, 440, 350, 270, 250, 220, 150, 80 ]

keresett_termek = input("Írd be a keresett termék nevét: ")
if keresett_termek in termek:
    index = termek.index(keresett_termek)
    print(egyseg[index])
else:
    print("Nincs ilyen termék")


# 2. feladat
# ▪ Vezessen be egy üres listát 'változás' azonosítóval!
# ▪ Vezessen be egy index változót, amivel az aktuális szám sorrendjét számolja
# ▪ Egy megfelelő ciklus segítségével járja végig egyszerre a két listát!
#     ▪ Számítsa ki a két értékpár százalékát az alábbi képlet segítségével:
#     ▪ 'százalék' legyen (decemberi / novemberi - 1) * 100
#     ▪ Kerekítse két tizedesjegyre a 'round(százalék, 2)' függvény használatával!
#     ▪ Füzze az eredményt a 'változás' lista végéhez!
# ▪ A ciklus után írja képernyőre a kiszámolt adatokat!

valtozas = []
index = 0
for index in range(len(december)):
    szazalek = (december[index] / november[index] - 1) * 100
    szazalek = round(szazalek, 2)
    valtozas.append(szazalek)
print(valtozas)

# 3. feladat
# ▪ importálja a json modult!
# ▪ készítsen az adatokból szótárat
# ▪ mentse fájlba data.json néven!

adatok = []
for index in range(len(termek)):
    adat = {}
    adat["termek"] = termek[index]
    adat["egyseg"] = egyseg[index]
    adat["december"] = december[index]
    adat["november"] = november[index]
    adat["valtozas"] = valtozas[index]
    adatok.append(adat)

with open("data.json", "w", encoding="utf8") as fájl:
    fájl.write(json.dumps(adatok, indent=4))