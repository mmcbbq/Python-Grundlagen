# Gegeben ist das folgende Dictionary my_dict: {'A': 1, 'B': 2, 'C': 3}. Schreibe eine Schleife, die jeden Schlüssel-Wert-Paar in my_dict ausgibt.
my_dict = {'A': 1, 'B': 2, 'C': 3}
for key, val in my_dict.items():
	print(f'{key}:{val}')

# Schreibe eine Schleife, die alle Schlüssel in my_dict ausgibt.
for key in my_dict.keys():
	print(key)
# Schreibe eine Schleife, die alle Werte in my_dict ausgibt.
for val in my_dict.values():
	print(val)
# Schreibe eine Schleife, die den Gesamtwert aller Werte in my_dict berechnet.
summe = 0
for val in my_dict.values():
	summe += val
print("Summe", summe)
# Schreibe eine Schleife, die jeden Schlüssel in my_dict ausgibt, dessen Wert größer als 1 ist.
for key, val in my_dict.items():
	if val > 1:
		print(key)

# Schreibe eine Schleife, die jeden Wert in my_dict verdoppelt und das aktualisierte Dictionary ausgibt.
for key, val in my_dict.items():
	my_dict[key] = 2 * my_dict[key]
print(my_dict)

# Gegeben ist das folgende Dictionary student_scores: {'Alice': [80, 90, 70], 'Bob': [85, 88, 75], 'Charlie': [90, 82, 88]}.
# Schreibe eine Schleife, die den Durchschnitt der Noten für jeden Schüler berechnet und ausgibt.
student_score = {'Alice': [95, 95, 95], 'Bob': [85, 98, 75], 'Charlie': [90, 100, 88]}

for key, val, in student_score.items():
	summe = 0
	z = 0
	for zahl in val:
		summe += zahl
		z += 1
	print(key, summe / z)

# Schreibe eine Schleife, die den Namen des Schülers mit der höchsten Gesamtnote aus dem Dictionary student_scores ausgibt.
beste = student_score['Alice'][0]
name = ""
for key, val, in student_score.items():
	for zahl in val:
		if zahl > beste:
			beste = zahl
			name = key
print(name)
# Schreibe eine Schleife, die das maximale Ergebnis für jeden Schüler aus dem Dictionary student_scores ausgibt.
for key, val in student_score.items():
	max_note = student_score[key][0]
	for note in val:
		if note > max_note:
			max_note = note
	print(f"{key}  beste Note {max_note}")

# Schreibe eine Schleife, die das minimale Ergebnis für jeden Schüler aus dem Dictionary student_scores ausgibt.
for key, val in student_score.items():
	min_note = student_score[key][0]
	for note in val:
		if note < min_note:
			min_note = note
	print(f"{key}  schlechte Note {min_note}")
# Schreibe eine Schleife, die den Namen des Schülers mit dem höchsten Durchschnitt aus dem Dictionary student_scores ausgibt.
bester = ""
bester_duch = 0
for key, val in student_score.items():
	summe = 0
	z = 0
	for note in val:
		summe += note
		z += 1
	duch = summe / z
	if duch > bester_duch:
		bester_duch = duch
		bester = key
print(f'Der beste Student ist {bester} mit einem Durchschnitt von {bester_duch}')

# Gegeben ist das folgende Dictionary inventory: {'Apfel': 10, 'Banane': 5, 'Orange': 8}.
# Schreibe eine Schleife, die den Namen der Frucht mit dem höchsten Bestand ausgibt.
inventory = {'Apfel': 10, 'Banane': 5, 'Orange': 8}
h_bestand = 0
namen = ""
for x, y in inventory.items():
	if y > h_bestand:
		h_bestand = y
		namen = x
print(namen, h_bestand)

# Schreibe eine Schleife, die den Namen und den Bestand jeder Frucht in inventory ausgibt.
for x, y in inventory.items():
	print(f'Name:{x} Bestand:{y}')

# Schreibe eine Schleife, die den Gesamtwert aller Früchte im inventory berechnet.
preise = {'Apfel': 0.50, 'Banane': 0.3, 'Orange': 1.1}
summe = 0
for x, y in inventory.items():
	summe += (y * preise[x])
print(summe)

my_dict = {1: {"name": "Apfel","anzahl": 10, 'preis': 0.5}, 2: {'name': "Banane","anzahl": 5, "preis": 0.3}, 3: {"name": "Orange","anzahl": 8, "preis": 1.1}}
summe = 0
for index, frut_dict in my_dict.items():
	summe += frut_dict["anzahl"] * frut_dict["preis"]
print(summe)


# Gegeben ist das folgende Dictionary sales: {'Apfel': 100, 'Banane': 150, 'Orange': 200}. Schreibe eine Schleife, die den Gesamtwert aller verkauften Früchte basierend auf den Verkaufszahlen in sales und den Preisen in preise berechnet.
sales = {'Apfel': 100, 'Banane': 150, 'Orange': 200, "Traube" : 400}
preise = {'Apfel': 0.50, 'Banane': 0.3, 'Orange': 1.1}
inventory = {'Apfel': 10, 'Banane': 5, 'Orange': 8, "Traube" : 200}

summe = 0
# for x, y in sales.items():
# 	summe += (y * preise[x])
# print(summe)
# Schreibe eine Schleife, die die Früchte ausgibt, die sowohl im inventory als auch in sales enthalten sind.
for key in inventory:
	if key in sales:
		print(key)

# Schreibe eine Schleife, den bestand in Prozent ausgibt
verkauft = {'Apfel': 10, 'Banane': 5, 'Orange': 8, "Traube" : 200}
bestand = {'Apfel': 100, 'Banane': 150, 'Orange': 200, "Traube" : 400}
for x,y in bestand.items():
	print(f"{x} bestand liegt bei {(y-verkauft[x])/y*100}%")

# Gegeben sind die folgenden Dictionaries: dict1 = {'a': 1, 'b': 2, 'c': 3} und dict2 = {'b': 3, 'c': 4, 'd': 5}.
# Schreibe eine Schleife, die die gemeinsamen Schlüssel von dict1 und dict2 ausgibt.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
for key in dict1:
	if key in dict2:
		print(key)


# Schreibe eine Schleife, die ein neues Dictionary erstellt, das die Summe der Werte für jeden gemeinsamen Schlüssel in dict1 und dict2 enthält.
new_dict = {}
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
for key in dict1:
	if key in dict2:
		new_dict[key] = dict1[key] + dict2[key]
print(new_dict)
# Schreibe eine Schleife, die ein neues Dictionary erstellt, das die absoluten Differenzen der Werte für jeden gemeinsamen Schlüssel in dict1 und dict2 enthält.
new_dict = {}
for key in dict1:
	if key in dict2:
		new_dict[key] = abs(dict1[key] - dict2[key])
print(new_dict)


