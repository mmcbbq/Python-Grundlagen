# Liste der Schülernamen
students = ['Ali', 'Mehmet', 'Ali', 'Philipp', 'Sven', 'Alexander', 'Matrix', 'Mohamad', 'Peter', 'Alexander', 'Sascha',
			'Darius', 'Elsa', 'Coskun', 'Grigorius', 'Kaycee', 'Carsten', 'Bader', 'Athanasios']
# Schleife, um jeden Schülernamen in der Liste zu begrüßen
for vorname in students:
	print('Hallo', vorname)
# Schleife, um die Anzahl der Buchstaben für jeden Schülernamen auszugeben
for vorname in students:
	print('Der Name', vorname, 'hat', len(vorname), 'Buchstaben')
# Schleife, um nur die Schüler mit einem Namen von 5 Buchstaben zu begrüßen
for vorname in students:
	if len(vorname) == 5:
		print('Hallo', vorname)
# Zählen der Anzahl von Schülern mit einem Namen von 5 Buchstaben


z = 0
for vorname in students:
	if len(vorname) == 5:  # Überprüfen, ob der Name 5 Buchstaben lang ist
		z += 1  # Wenn ja, inkrementiere den Zähler um 1
print(z)

print(list(enumerate(students)))
# Berechnung der Summe der Zahlen in einer Liste
zahlen = [12, 15, 18, 2]
summe = 0  # Initialisierung einer Summenvariable AUSSERHALB DER SCHLEIFE
for zahl in zahlen:
	summe = summe + zahl
print(summe)

print(sum(zahlen))
# zahl = 12
# summe = 0 + 12 -> summe = 12

# zahl = 15
# summe = 12 + 15 -> summe = 27

# zahl = 18
# summe = 27 + 18 -> summe = 45

# zahl = 2
# summe = 45 + 2 -> summe = 47


# Liste von Zahlen
zahlen = [12, 10, 8, 4, 15, 18, 2, 8, 11]
liste = []
for zahl in zahlen:  # Füge Zahl zur Liste hinzu, wenn sie kleiner oder gleich 10 ist
	if zahl <= 10:
		liste.append(zahl)
print(liste)  # Ausgabe der Liste mit Zahlen kleiner oder gleich 10
# Liste von Schülern
students = ['Ali', 'Mehmet', 'Ali', 'Philipp', 'Sven', 'Alexander', 'Matrix', 'Mohamad', 'Peter', 'Alexander', 'Sascha',
			'Darius', 'Elsa', 'Coskun', 'Grigorius', 'Kaycee', 'Carsten', 'Bader', 'Athanasios']
z = 0
# Schleife, um jeden Schülernamen nacheinander zu wiederholen
for name in students:
	print(name * z)  # Jeder Name wird entsprechend seines Index in der Liste wiederholt
	z += 1
#  Schleife, um Schülernamen zu finden, die mit 'A' oder 'a' beginnen
for name in students:
	if name[0].upper() == 'A':  # Überprüfe, ob der erste Buchstabe des Namens 'A' oder 'a' ist
		print(name)  # Drucke den Namen, wenn er mit 'A' oder 'a' beginnt

# Schleife, um Schülernamen zu finden, die den Buchstaben 'i' enthalten
for name in students:
	for buchstabe in name:
		if buchstabe == 'i':
			print(name)
			break  # Beende die innere Schleife, wenn der Buchstabe gefunden wurde

list1 = [22, 27, 31, 19, 47, 89, 22, 79, 26, 27]
list2 = [71, 6, 47, 19, 94, 71, 65, 67, 19, 64]
list3 = [19, 14, 34, 86, 86, 31, 97, 6, 21, 21]

nested_list = [list1, list2, list3]
sieb = []
# alle Zahlen die ohne rest durch 3 Teilbar sind. In die Liste Sieb
for list in nested_list:
	for zahl in list:
		if zahl % 3 == 0:
			sieb.append(zahl)
print(sieb)
