numbers = [65, 44, 77, 58, 38, 56, 77, 91, 18, 57, 67, 84, 12, 66, 43, 7, 53, 76, 66, 11, 44, 26, 34, 61, 98, 13, 55,
		   46, 29, 9, 78, 85, 14, 86, 18, 4, 98, 98, 10, 70, 32, 98, 83, 70, 24, 6, 30, 6, 98, 34, 81, 2, 96, 21, 4, 6,
		   84, 20, 39, 59, 3, 84, 71, 30, 29, 27, 25, 21, 68, 76, 70, 57, 98, 53, 84, 63, 34, 26, 40, 38, 71, 92, 64,
		   78, 9, 1, 30, 25, 70, 85, 11, 77, 31, 41, 23, 59, 100, 45, 5, 94]

# Gebe alle Zahlen aus der numbers Liste aus die kleiner gleich 50 sind
for x in numbers:
	if x <= 50:
		print(x)

# Die Anzahl der Zahlen aus der numbers Liste die zwischen 30 und 70 liegen.
for x in numbers:
	if 30 <= x <= 70:
		print(x)

# Gebe alle Zahlen aus der numbers Liste die gerade durch 5 teilbar sind aus (modulo == 0)
for x in numbers:
	if x % 5 == 0:
		print(x)

tim = ["k", 'e', '', "", 'on', 'on', 'on', 'onn', 'on', '', "", 'PR', 'xx', 'n', 'on', 'x', '', "", 'FE', 'x', 'x', 'x',
	   'x', '', "", 'x', 'on', 'k', 'e', 'x']
anzahl_buchstaben = {'x': 0, 'k': 0, 'on': 0, 'e': 0, '': 0, 'PR': 0, 'FE': 0, 'fehleingabe': []}
for x in tim:
	if x in anzahl_buchstaben:
		anzahl_buchstaben[x] += 1
	else:
		anzahl_buchstaben['fehleingabe'].append(x)

print(anzahl_buchstaben)

# In der liste Tim sollen alle Werte gezaehlt werden. Nutze zum Zaehlen das anzahl_buchstaben dict.
# Ausgabe
for key, val in anzahl_buchstaben.items():
	if key == '':
		print(f"'' = {val}")
	else:
		print(f'{key} = {val}')
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
anzahl_a = 0
anzahl_m = 0
for name in students:
	for buchstabe in name:
		if buchstabe.lower() == 'a':
			anzahl_a += 1
		if buchstabe.lower() == 'm':
			anzahl_m += 1
print(anzahl_m)
print(anzahl_a)
# Erstelle ein dict in dem der Buchstabe "Key" (case-insensitive) und die Anzahl "Value" aller Namen gespeichert werden.
anzahl_buchstaben = {}
for name in students:
	for buch in name:
		if buch.lower() not in anzahl_buchstaben.keys():
			anzahl_buchstaben[buch.lower()] = 1
		else:
			anzahl_buchstaben[buch.lower()] += 1
print(anzahl_buchstaben)

allenamen = ""
for x in students:
	allenamen += x

allenamen = allenamen.lower()
print(allenamen)
for x in allenamen:
	for ascii in range(97, 123):
		anzahl_buchstaben[chr(ascii)] = allenamen.count(chr(ascii))
print(anzahl_buchstaben)
