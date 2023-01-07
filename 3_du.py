import json, math, sys
from pyproj import Transformer

#výpočet vzdálenosti
def vypocet_vzdalenosti (x_k, y_k, x_a, y_a):
    hodnota = (x_k - x_a)**2 + (y_k - y_a)**2
    return math.sqrt(hodnota)

#Přečtení geojson souborů
with open("adresy.geojson", encoding="utf-8") as f:
    adresy = json.load(f)
    print(adresy)

with open("kontejnery.geojson", encoding="utf-8") as f:
    kontejnery = json.load(f)
    print(kontejnery)

#převod z WGS na JTSK
wgs2jtsk = Transformer.from_crs(4326,5514,always_xy=True)

kontejnery_souradnice_jtsk = []
adresy_souradnice_jtsk = []

for f in adresy['features']:
        x_a = f['geometry']['coordinates'][0]
        y_a = f['geometry']['coordinates'][1]

        jtsk_adresy = wgs2jtsk.transform(x_a,y_a)
        adresy_souradnice_jtsk.append(jtsk_adresy)
print (adresy_souradnice_jtsk)   

for f in kontejnery['features']:
    x_k = f['geometry']['coordinates'][0]
    y_k = f['geometry']['coordinates'][1]
    jtsk_adresy = x_k,y_k 
    kontejnery_souradnice_jtsk.append(jtsk_adresy)
print (kontejnery_souradnice_jtsk)

seznam_nejmensi_vzdalenosti = []
# funkce na výpočet nejmenších vzdaleností uživatelem zvolených adres ke kontejnerům v Praze  
def vypocet_nejmensich_vzdalenosti(adresy):
    for adresa in adresy:
        nejmensi_vzdalenost = 10000
        for kontejner in kontejnery_souradnice_jtsk:
            vzdalenost = vypocet_vzdalenosti(adresa[0], adresa[1], kontejner[0], kontejner[1])
            if (vzdalenost <= nejmensi_vzdalenost): 
                nejmensi_vzdalenost = vzdalenost
        if (nejmensi_vzdalenost == 10000): 
            sys.exit("Nebyl nalezen kontejner do vzálenosti 10 km")
        else: seznam_nejmensi_vzdalenosti.append(nejmensi_vzdalenost)

vypocet_nejmensich_vzdalenosti (adresy_souradnice_jtsk)
print (seznam_nejmensi_vzdalenosti)


def vypocet_prumerne_min_vzdalenosti(vzdalenosti):
    suma = 0
    for vzdalenost in vzdalenosti:
        suma += vzdalenost
    prumer = suma/len(vzdalenosti)
    print (prumer)
    return prumer
    
vypocet_prumerne_min_vzdalenosti(seznam_nejmensi_vzdalenosti)