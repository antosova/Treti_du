import csv

# Otevřeme a přečteme soubor Data_prutok.csv
"""with open("Data_prutok.csv", encoding="utf-8", newline='') as f:
	reader = csv.reader(f, delimiter=",")
	for row in reader:
		print(row)

with open("Data_prutok.csv", encoding="utf-8", newline='') as f:
	reader = csv.reader(f, delimiter=",")
	for row in range(7):
		(prutoky) = (next(reader)[3])
		print (prutoky)

prutoky_list = []
prutoky_list.append(prutoky)
print(prutoky_list)
#def průměr_7(součet_průtoků, pocet_prutoků):"""

suma_tyden = 0
suma_rok = 0
index = 1
with open("Data_prutok.csv", encoding="utf-8", newline='') as f:
	reader = csv.reader(f, delimiter=",")
	for row in reader:
		suma_tyden+= row[3]
		suma_rok+= row[3]

		if index % 7 == 0:
			print (suma_tyden/7)
			suma_tyden = 0
		
		if index % 365:
			print (suma_rok/365)
			suma_tyden = 0
		index+=1
		
#druhej commit zkouska
			
   
