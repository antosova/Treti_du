import json
#from pyproj import Transformer
#Přečtení geojson souborů
with open("adresy.geojson", encoding="utf-8") as f:
    adresy = json.load(f)
    print(adresy)

with open("kontejnery.geojson", encoding="utf-8") as f:
    kontejnery = json.load(f)
    print(kontejnery)