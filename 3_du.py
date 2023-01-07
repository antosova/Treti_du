import json
from pyproj import Transformer

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