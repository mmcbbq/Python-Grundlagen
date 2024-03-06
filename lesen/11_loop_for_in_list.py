students = ['Ali', 'Mehmet', 'Ali', 'Philipp', 'Sven', 'Alexander', 'Matrix', 'Mohamad', 'Peter', 'Alexander', 'Sascha',
			'Darius', 'Elsa', 'Coskun', 'Grigorius', 'Kaycee', 'Carsten', 'Bader', 'Athanasios']

for vorname in students:
	print('Hallo', vorname)

for vorname in students:
	print('Der Name', vorname, 'hat', len(vorname), 'Buchstaben')

for vorname in students:
	if len(vorname) == 5:
		print('Hallo', vorname)



z = 0
for vorname in students:
	if len(vorname) == 5:
		z += 1
print(z)

print(list(enumerate(students)))

zahlen = [12, 10, 8, 4, 15, 18, 2, 8, 11]
summe = 0
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
zahlen = [12, 10, 8, 4, 15, 18, 2, 8, 11]
liste = []
for zahl in zahlen:
	if zahl <= 10:
		liste.append(zahl)
print(liste)

students = ['Ali', 'Mehmet', 'Ali', 'Philipp', 'Sven', 'Alexander', 'Matrix', 'Mohamad', 'Peter', 'Alexander', 'Sascha',
			'Darius', 'Elsa', 'Coskun', 'Grigorius', 'Kaycee', 'Carsten', 'Bader', 'Athanasios']
z = 1
for name in students:
	print(name * z)
	z += 1
for name in students:
	if name[0].upper() == 'A':
		print(name)

for name in students:
	for buchstabe in name:
		if buchstabe == 'i':
			print(name)
			break # Stop die Schleife

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





