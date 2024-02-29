# Schreibe eine Python-Funktion, die den Bubblesort-Algorithmus verwendet,
# um eine Liste von Zahlen in aufsteigender Reihenfolge zu sortieren.
# Der Bubblesort-Algorithmus funktioniert, indem er benachbarte Elemente vergleicht
# und sie vertauscht, wenn sie in der falschen Reihenfolge sind.
# Dieser Prozess wird so lange wiederholt, bis die gesamte Liste sortiert ist.

# liste = [27, 29, 7, 76, 56]

liste = [40, 8, 63, 60, 12, 4, 13, 82, 87, 87, 87, 84, 85, 39, 57, 55, 72, 6, 46, 18, 5, 97, 78, 64, 94, 64, 62, 22, 11,
		 89, 92, 53, 22, 51, 44, 49, 6, 87, 57, 20, 39, 67, 87, 49, 71, 79, 80, 94, 19, 57, 13, 71, 51, 99, 68, 31, 80,
		 63, 41, 17, 25, 7, 88, 86, 29, 58, 99, 63, 28, 59, 2, 34, 15, 73, 36, 90, 9, 75, 61, 40, 1, 23, 71, 94, 75, 46,
		 59, 72, 73, 63, 93, 90, 68, 7, 29, 92, 44, 74, 84, 80]

for y in range(len(liste) - 1):
	print(f'start outer loop {y}')
	for x in range(len(liste) - 1 - y):
		print(liste[x], liste[x + 1], 'vergleich')
		if liste[x] > liste[x + 1]:
			liste[x], liste[x + 1] = liste[x + 1], liste[x]

			# zwischen = liste[x]
			# liste[x] = liste[x + 1]
			# liste[x + 1] = zwischen

			print('getauscht')
		else:
			print('nicht getauscht')
		print(liste)
	print('outer loop end')

# for k in range(len(liste) - 1):
# 	for zahl in range(len(liste) - 1 - k):
# 		if liste[zahl] > liste[zahl + 1]:
# 			liste[zahl], liste[zahl + 1] = liste[zahl + 1], liste[zahl]
# print(liste)
