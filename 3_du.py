import json, math, sys, re
from pyproj import Transformer

try:
    # Převod z WGS na JTSK a vytvoření seznamů souřadnice.
    wgs2jtsk = Transformer.from_crs(4326,5514,always_xy=True)

    kontejnery_jtsk = []
    adresy_jtsk = []

    # Výpočet vzdálenosti
    def vypocet_vzdalenosti (x_k, y_k, x_a, y_a):
        hodnota = (x_k - x_a)**2 + (y_k - y_a)**2
        return math.sqrt(hodnota)
    # Funkce, která domům s domovním kontejnerem, přiřadí vzdálenost nula.
    def Domovni_kontejnery(adresy):
        for kontejner in kontejnery_jtsk:
            if kontejner[2]:
                for adresa in adresy:
                    adresa_kontejneru = kontejner[3]
                    cislo_domu = str(adresa[2])
                    cislo_domu = re.sub(r'[^0-9/]', '', cislo_domu) # Pro porovnání adres je třeba upravit adresu domu regulárním výrazem.
                    
                    if adresa_domu == adresa_kontejneru:
                        adresa[3] = kontejner
                        adresa[3] = 0

    # Funkce pro výpočet nejmenších vzdáleností uživatelem zvolených adres ke kontejnerům v Praze.  
    def zjisteni_nejmensich_vzdalenosti(adresy):
        index = 0
        for adresa in adresy:
            if adresa[3] == 0:
                index = index+1
                continue
            nejmensi_vzdalenost = 10000
            for kontejner in kontejnery_jtsk:
                if kontejner[2]:
                    continue
                vzdalenost = vypocet_vzdalenosti(adresa[0][0], adresa[0][1], kontejner[0], kontejner[1])
                if (vzdalenost <= nejmensi_vzdalenost): 
                    nejmensi_vzdalenost = vzdalenost
            if (nejmensi_vzdalenost == 10000): 
                sys.exit("Nebyl nalezen kontejner do vzálenosti 10 km.")
            else:
                adresy_jtsk[index][3] = nejmensi_vzdalenost
            index = index+1

    # Funkce pro výpočet průměru nejmenších vzdáleností.
    def vypocet_prumeru_min_vzdalenosti(data):
        suma = 0
        for D in data:
            suma += D[3]
        prumer = suma/len(data)
        print ("Průměrná nejkratší vzdálenost je "+ str(round(prumer))+" metrů.")
        return prumer

    # Funkce pro nalezení maximální vzdálenosti k nejbližšímu kontejneru.
    def nalezeni_max_vzdalenosti(data):
        max = -1
        ulice_max = None
        cislo_popisne_max = None
        for D in data:
            if D[3] > max:
                max = D[3]
                ulice_max  = D[1]
                cislo_popisne_max = D[2]
        print("Nejdále ke kontejneru je to z adresy " + str(ulice_max) + " " + str(cislo_popisne_max)+ " a to " +str(round(max))+" metrů.")
        return max,ulice_max, cislo_popisne_max

    # Funkce pro nalezení mediánu.
    def median(data): 
        vzdalenosti = [item[3] for item in data]
        vzdalenosti.sort()
        stred = len(vzdalenosti)//2
        vysledek = (vzdalenosti[stred]+vzdalenosti[~stred])/2
        print("Medián vzdáleností je "+ str(round(vysledek)) + " metrů.")

    # Přečtení geojson souborů
    with open("adresy.geojson", encoding="utf-8") as f:
        adresy = json.load(f)

    with open("kontejnery.geojson", encoding="utf-8") as f:
        kontejnery = json.load(f)
    # Vytvoření seznamu adres a seznamu kontejnerů s potřebnými údaji
    for f in adresy['features']:
            x_a = f['geometry']['coordinates'][0]
            y_a = f['geometry']['coordinates'][1]
            ulice = f['properties']['addr:street']
            cislo_popisne = f['properties']['addr:housenumber']
            nejmensi_vzdalenosti = 10000

            souradnice_jtsk = wgs2jtsk.transform(x_a,y_a)
                
            adresy_info = [souradnice_jtsk,ulice,cislo_popisne,nejmensi_vzdalenosti]
            adresy_jtsk.append(adresy_info)

    for f in kontejnery['features']:
        x_k = f['geometry']['coordinates'][0]
        y_k = f['geometry']['coordinates'][1]
        domovni = False
        adresa = f['properties']['STATIONNAME']

        if f['properties']['PRISTUP'] == 'obyvatelům domu':
            domovni = True
        
        kontejnery_info = x_k,y_k,domovni,adresa
        kontejnery_jtsk.append(kontejnery_info)

    Domovni_kontejnery(adresy_jtsk) 
    zjisteni_nejmensich_vzdalenosti (adresy_jtsk)
    vypocet_prumeru_min_vzdalenosti(adresy_jtsk)
    nalezeni_max_vzdalenosti(adresy_jtsk)
    median(adresy_jtsk)

except FileNotFoundError:                                               
	print("Soubor není.")
except ZeroDivisionError:
    print("Dělení nulou")
except TypeError:
    print("špatný datová typ proměnné")
except json.decoder.JSONDecodeError:
    sys.exit("Chybný formát souboru")
except: 
	print("Něco se šíleně pokazilo.")