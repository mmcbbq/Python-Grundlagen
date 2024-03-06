numbers = [65, 44, 77, 58, 38, 56, 77, 91, 18, 57, 67, 84, 12, 66, 43, 7, 53, 76, 66, 11, 44, 26, 34, 61, 98, 13, 55, 46, 29, 9, 78, 85, 14, 86, 18, 4, 98, 98, 10, 70, 32, 98, 83, 70, 24, 6, 30, 6, 98, 34, 81, 2, 96, 21, 4, 6, 84, 20, 39, 59, 3, 84, 71, 30, 29, 27, 25, 21, 68, 76, 70, 57, 98, 53, 84, 63, 34, 26, 40, 38, 71, 92, 64, 78, 9, 1, 30, 25, 70, 85, 11, 77, 31, 41, 23, 59, 100, 45, 5, 94]

# Gebe alle Zahlen aus der numbers Liste aus die kleiner gleich 50 sind
for zahl in numbers:
	if zahl <= 50:
		print(zahl)

# Die Anzahl der Zahlen aus der numbers Liste die zwischen 30 und 70 liegen.
z = 0
for zahl in numbers:
	if 30 < zahl and zahl < 70:
		z += 1
print(z)

# Gebe alle Zahlen aus der numbers Liste die gerade durch 5 teilbar sind aus (modulo == 0)
for zahl in numbers:
	if zahl % 5 == 0:
		print(zahl)



tim = ["k", 'e', '', "", 'on', 'on', 'on', 'on', 'on', '', "", 'PR', 'x', 'n', 'on', 'x', '', "", 'FE', 'x', 'x', 'x',
	   'x', '', "", 'x', 'on', 'k', 'e', 'x']

# In der liste Tim sollen alle Werte gezaehlt werden
# Ausgabe
# k = 5
# x =10
# on = 6
# e = 8
# '' = 4
# PR = 5
# FE = 3
# fehleingabe = [onn, xx, PJ]



students = ['Ali', 'Mehmet', 'Ali', 'Philipp', 'Sven', 'Alexander', 'Matrix', 'Mohamad', 'Peter', 'Alexander', 'Sascha',
			'Darius', 'Elsa', 'Coskun', 'Grigorius', 'Kaycee', 'Carsten', 'Bader', 'Athanasios']
# Zaehle alle "a" in den Namen (case-insensitive)

# Zaehle alle "m" in den Namen

# Erstelle 2 Listen buchstaben und anzahl
# in der Liste buchstaben sollen alle Buchstaben, die in den Namen vorkommen rein
# und in der Liste anzahl wie oft sie vorkommen (case-insensitive)
# Die Buchstaben und die Anzahl mueseen denselben index haben
buchstaben = []
anzahl = []
count = ""
for name in students:
	z = 0
	print(f"count {name}")
	for buch in name:
		if buch.upper() in buchstaben:
			continue
		else:
			print(f"{buch} nicht in liste")
			z = 0
			for name_check in students:
				for b_add in name_check:
					if b_add.upper() == buch.upper():
						z += 1
			buchstaben.append(buch.upper())
			anzahl.append(z)
print(len(buchstaben), )
print(len(anzahl))
print(dict(zip(buchstaben, anzahl)))



