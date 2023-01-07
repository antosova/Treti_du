import json, math, sys
from pyproj import Transformer

#Přečtení geojson souborů
with open("adresy.geojson", encoding="utf-8") as f:
    adresy = json.load(f)
    print(adresy)

with open("kontejnery.geojson", encoding="utf-8") as f:
    kontejnery = json.load(f)
    print(kontejnery)

#převod z WGS na JTSK a vytvoření seznamů souřadnice
wgs2jtsk = Transformer.from_crs(4326,5514,always_xy=True)

kontejnery_souradnice_jtsk = []
adresy_souradnice_jtsk = []

for f in adresy['features']:
        x_a = f['geometry']['coordinates'][0]
        y_a = f['geometry']['coordinates'][1]
        ulice = f['properties']['addr:street']
        cislo_popisne = f['properties']['addr:housenumber']
        nejmensi_vzdalenosti = 0

        jtsk_adresy = wgs2jtsk.transform(x_a,y_a)
            
        adresy_info = [jtsk_adresy,ulice,cislo_popisne,nejmensi_vzdalenosti]
        adresy_souradnice_jtsk.append(adresy_info)
print (adresy_souradnice_jtsk)   

for f in kontejnery['features']:
    x_k = f['geometry']['coordinates'][0]
    y_k = f['geometry']['coordinates'][1]
    jtsk_adresy = x_k,y_k 
    kontejnery_souradnice_jtsk.append(jtsk_adresy)
print (kontejnery_souradnice_jtsk)

#výpočet vzdálenosti
def vypocet_vzdalenosti (x_k, y_k, x_a, y_a):
    hodnota = (x_k - x_a)**2 + (y_k - y_a)**2
    return math.sqrt(hodnota)

seznam_nejmensi_vzdalenosti = []
# funkce na výpočet nejmenších vzdaleností uživatelem zvolených adres ke kontejnerům v Praze  
def vypocet_nejmensich_vzdalenosti(adresy):
    index = 0
    for adresa in adresy:
        nejmensi_vzdalenost = 10000
        for kontejner in kontejnery_souradnice_jtsk:
            vzdalenost = vypocet_vzdalenosti(adresa[0][0], adresa[0][1], kontejner[0], kontejner[1])
            if (vzdalenost <= nejmensi_vzdalenost): 
                nejmensi_vzdalenost = vzdalenost
        if (nejmensi_vzdalenost == 10000): 
            sys.exit("Nebyl nalezen kontejner do vzálenosti 10 km")
        else:
            adresy_souradnice_jtsk[index][3] = nejmensi_vzdalenost
        index = index+1


vypocet_nejmensich_vzdalenosti (adresy_souradnice_jtsk)
print (adresy_souradnice_jtsk)

# funkce na výpočet průměru nejmenších vzdaleností
def vypocet_prumeru_min_vzdalenosti(data):
    suma = 0
    for D in data:
        suma += D[3]
    prumer = suma/len(data)
    print (prumer)
    return prumer
    
vypocet_prumeru_min_vzdalenosti(adresy_souradnice_jtsk)

#funkce na výpočet maximální vzdálenosti k nejbližšímu kontejneru
def vypocet_max_vzdalenosti(data):
    max = -1
    ulice_max = None
    cislo_popisne_max = None
    for D in data:
        if D[3] > max:
            max = D[3]
            ulice_max  = D[1]
            cislo_popisne_max = D[2]
    print(max)
    print(ulice_max)
    print(cislo_popisne_max)
    return max,ulice_max, cislo_popisne_max

vypocet_max_vzdalenosti(adresy_souradnice_jtsk)