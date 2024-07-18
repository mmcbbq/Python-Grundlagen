# Gegeben ist das folgende Dictionary my_dict: {'A': 1, 'B': 2, 'C': 3}. Schreibe eine Schleife, die jedes Schlüssel-Wert-Paar in my_dict ausgibt.
my_dict = {'A': 1, 'B': 2, 'C': 3}
for key, val in my_dict.items():
	print(f'{key}: {val}')
print("-" * 30)
# Schreibe eine Schleife, die alle Schlüssel in my_dict ausgibt.
for key in my_dict.keys():
	print(f'{key}')
print("-" * 30)
# Schreibe eine Schleife, die alle Werte in my_dict ausgibt.
for val in my_dict.values():
	print(f'{val}')
print("-" * 30)
# Schreibe eine Schleife, die den Gesamtwert aller Werte in my_dict berechnet.
summe = 0
for val in my_dict.values():
	summe += val

print(summe)
print("-" * 30)
# Schreibe eine Schleife, die jeden Schlüssel in my_dict ausgibt, dessen Wert größer als 1 ist.
for key, val in my_dict.items():
	if val > 1:
		print(key)
print("-" * 30)
# Schreibe eine Schleife, die jeden Wert in my_dict verdoppelt und das aktualisierte Dictionary ausgibt.
for key, val in my_dict.items():
	my_dict[key] = val * 2
print(my_dict)

print("-" * 30)
# Gegeben ist das folgende Dictionary student_scores: {'Alice': [80, 90, 70], 'Bob': [85, 88, 75], 'Charlie': [90, 82, 88]}. Schreibe eine Schleife, die den Durchschnitt der Noten für jeden Schüler berechnet und ausgibt.
student_scores = {'Alice': [80, 90, 70], 'Bob': [85, 88, 75], 'Charlie': [90, 82, 88]}
for student, noten in student_scores.items():
	summe = 0
	anzahl = 0
	for note in noten:
		summe += note
		anzahl += 1
	print(f'{student} {summe / anzahl:.2f}')
print("-" * 30)

# Schreibe eine Schleife, die den Namen des Schülers mit der höchsten Gesamtnote aus dem Dictionary student_scores ausgibt.
# best = list(student_scores.keys())[0]
best_student = "Alice"
best_punkte = 0

for student, noten in student_scores.items():
	summe =0
	for punkt in noten:
		summe += punkt
	if summe > best_punkte:
		best_punkte = summe
		best_student = student
print(best_student)
print("-" * 30)

# Schreibe eine Schleife, die das maximale Ergebnis für jeden Schüler aus dem Dictionary student_scores ausgibt.
# Schreibe eine Schleife, die das minimale Ergebnis für jeden Schüler aus dem Dictionary student_scores ausgibt.
for keys, values in student_scores.items():
	min_wert = values[0]
	max_wert = values[0]
	for note in values:
		if note > max_wert:
			max_wert = note
		elif note < min_wert:
			min_wert = note
	print(f'{keys} {min_wert} {max_wert}')
print("-" * 30)

# Schreibe eine Schleife, die den Namen des Schülers mit dem höchsten Durchschnitt aus dem Dictionary student_scores ausgibt.

best_student = "Alice"
best_durchschnitt = 0

for student, noten in student_scores.items():
	summe =0
	zahler = 0
	for punkt in noten:
		summe += punkt
		zahler += 1
		durchschnitt = summe/ zahler
	if durchschnitt > best_durchschnitt:
		best_durchschnitt = durchschnitt
		best_student = student
print(f'Der beste student ist {best_student} mit einem durschnitt von {best_durchschnitt:.2f}	')

print("-" * 30)


# Gegeben ist das folgende Dictionary . Schreibe eine Schleife, die den Namen der Frucht mit dem höchsten Bestand ausgibt.
fruits = {'Apfel': {'bestand': 100, 'verkauft': 20, 'preis': 0.25, 'lager kapazität': 200},
		  'Banane': {'bestand': 78, 'verkauft': 42, 'preis': 0.12, 'lager kapazität': 100},
		  'Orange': {'bestand': 24, 'verkauft': 11, 'preis': 0.39, 'lager kapazität': 50}
		  }
name = ''
max_bestand = 0
for key, val in fruits.items():
	if val['bestand'] > max_bestand:
		max_bestand = val['bestand']
		name = key
print(f'Der höchste Bestand von {max_bestand} hat der {name}')

print("-" * 30)

# erweitere fruits um den Eintrag 'Traube: {'bestand': 150, 'verkauft': 0, 'preis': 0.59, 'lager kapazität': 150}
fruits['Traube'] = {'bestand': 150, 'verkauft': 0, 'preis': 0.59, 'lager kapazität': 150}
# Schreibe eine Schleife, die den Namen und den Bestand jeder Frucht in fruits ausgibt.
for key, val in fruits.items():
	print(f'{key}:\t {val["bestand"]} ')
# Schreibe eine Schleife, die den Wert der Fruechte in bestand sowie den wert der verkauften Fruechte ausgibt.
for fruit, liste in fruits.items():
	print(f'{fruit}: Bestandwert {liste["bestand"] * liste["preis"]} Einnahmen {liste["verkauft"] * liste["preis"]}')
# Berechne die auslastung der lager Kapazität in % fuer alle Fruechte.
for fruit , liste in fruits.items():
	print(f'{fruit}: {liste["bestand"]*100 / liste["lager kapazität"]}%')
# Gegeben sind die folgenden Dictionaries: dict1 = {'a': 1, 'b': 2, 'c': 3} und dict2 = {'b': 3, 'c': 4, 'd': 5}. Schreibe eine Schleife, die die gemeinsamen Schlüssel von dict1 und dict2 ausgibt.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print('-'*30)
for key in dict1:
	if key in dict2:
		print(key)
# Schreibe eine Schleife, die ein neues Dictionary erstellt, das die Summe der Werte für jeden gemeinsamen Schlüssel in dict1 und dict2 enthält.
print('-'*30)
summe_dict = {}
for key in dict1:
	if key in dict2:
		summe_dict[key] = dict1[key] + dict2[key]
print(summe_dict)
print('-'*30)
# Schreibe eine Schleife, die ein neues Dictionary erstellt, das die absoluten Differenzen der Werte für jeden gemeinsamen Schlüssel in dict1 und dict2 enthält.
diff_dict = {}
for key in dict1:
	if key in dict2:
		diff_dict[key] = abs(dict1[key] - dict2[key])
print(diff_dict)

