Program pro nalezení nejbližšího kontejneru v Praze k domovním adresám 

Tento program slouží k zhodnocení dostupnosti kontejnerů na tříděný odpad v jednotlivých čtvrtích Prahy. 

Vstupní data kontejnerů:
- soubor z pražského Geoportálu dostupný na adrese https://www.geoportalpraha.cz/cs/data/otevrena-data/8726EF0E-0834-463B-9E5F-FE09E62D73FB
- obsahuje souřadnice, na kterých se nachází kontejnery na tříděný odpad souřadnicovém systému S-JTSK
- dále se v datech nachází informace, zda jsou kontejnery volně přístupné, či domovní (přístupné pouze obyvatelům daného domu)
- jedná se o soubor formátu GeoJSON a musí se jmenovat kontejnery.geojson

Vstupní data domovních adres:
- soubor dostupný na adrese https://overpass-turbo.eu/
- obsahuje adresní body Vámi vybrané čtvrti v Praze v souřadnicovém systému WGS-84
- jedná se o názvy ulic, čísla popisná a jejich vlastnosti spolu s jejich souřadnicemi
- data obět stáhneme jako GeoJSON a pojmenujeme adresy.geojson

Po načtení těchto vstupních dat program nalezne vzdálenost od každé domovní adresy k nejbližšímu kontejneru. Poté vypíše průměr z těchto vzdáleností a z jaké adresy je to k nejbližšímu kontejneru nejdále a o jakou vzdálenost se jedná.
K těmto informacím navíc nalezne a vypíše medián vzdáleností. 

Program zohledňuje kontejnery, které jsou privátní (tzv. domovní kontejnery). Tyto kontejnery jsou přístupné pouze lidem, kteří na dané adrese bydlí. Pro ostatní obyvatele čtvrti jsou nedostupné. 

Program převádí souřadnice domovních adres ze souřadnicového systému WGS do S - JTSK. Výsledné vzdálenosti adres od kontejnerů jsou v S - JTSK. 




# Zkouska
