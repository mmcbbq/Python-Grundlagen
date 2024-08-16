# Schreibe eine Funktion 'get_durchschnitt', die eine Liste von Zahlen erhaelt und den Durchschnitt
# dieser Liste returned
zahlen = [10, 20, 30, 40, 50]


def get_durchschnitt(liste):
	summe = 0
	z = 0
	for x in liste:
		summe += x
		z += 1
	d = summe / z
	return d


print(get_durchschnitt(zahlen))


# Schreibe eine Funktion 'get_durchschnitt_unbekannt', die eine unbestimmte Anzahl von Parametern  von Zahlen erhaelt
# und den Durchschnitt dieser Parameter returned

def get_durchschnitt_unbekannt(*zahlen):
	summe = 0
	z = 0
	for x in zahlen:
		summe += x
		z += 1
	d = summe / z
	return d


print(get_durchschnitt_unbekannt(10, 20, 30, 40, 50, 24, 24, 446, 7, 8, 9, 3))

# Schreibe eine Funktion, die eine Liste von Zahlen nimmt
# und eine neue Liste mit den Quadraten dieser Zahlen zurückgibt
zahlen = [2, 4, 6, 8, 10]  # -> # Sollte [4, 16, 36, 64, 100] ergeben


def quadrat_list(liste):
	q_liste = []
	for x in liste:
		q_liste.append(x ** 2)
	return q_liste


print(quadrat_list(zahlen))


# Schreibe eine Funktion, die eine unbestimmte Anzahl von Parametern von Zahlen nimmt
# und eine Liste mit den Quadraten dieser Zahlen zurückgibt
def quadrat_list_unbekannt(*liste):
	q_liste = []
	for x in liste:
		q_liste.append(x ** 2)
	return q_liste


print(quadrat_list_unbekannt(2, 4, 6, 8, 10))


# Schreibe eine Funktion,
# die das Maximum und das Minimum aus einer
# Liste von Zahlen zurückgibt. (wenn es geht ohne min() und max())
# return [ min ,max]
# def min_max(liste):
# 	return [min(liste),max(liste)]
def min_max(liste):
	min_wert = liste[0]
	max_wert = liste[0]
	for x in liste:
		if x > max_wert:
			max_wert = x
		if x < min_wert:
			min_wert = x
	return [min_wert, max_wert]


print(min_max(zahlen))

# Schreibe die Funktionen zur Überprüfung der Sieg bedingungen des Tic Tac Toe spiels.
# Sie sollen True zurückgeben bei einem Sieg und False wenn sie nicht erfüllt werden

spielfeld = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


# waagerechter Sieg
# [x, x, x]
# [-, o, o]
# [o, -, o]
def sieg_w(feld):
	for inner_list in feld:
		if inner_list[0] == inner_list[1] and inner_list[0] == inner_list[2] and inner_list[0] != '-':
			return True
	return False


# senkrechter Sieg
# [x, x, o]
# [-, o, o]
# [o, -, o]
def sieg_s(feld):
	for x in range(3):
		if feld[0][x] == feld[1][x] and feld[0][x] == feld[2][x] and feld[0][x] != "-":
			return True
	return False


# diagonaler Sieg oben links nach unten Rechts
# [o, x, x]
# [-, o, o]
# [o, -, o]

def sieg_dlr(feld):
	if feld[0][0] == feld[1][1] and feld[0][0] == feld[2][2] and feld[0][0] != "-":
		return True
	return False


# diagonaler Sieg unten links nach oben Rechts
# [x, x, o]
# [-, o, o]
# [o, -, o]
def sieg_drl(feld):
	if feld[0][2] == feld[1][1] and feld[0][2] == feld[2][0] and feld[1][1] != "-":
		return True
	return False


# Test
spielstande = [
	[['x', 'x', 'x'], ['-', 'o', 'o'], ['o', '-', 'o']],
	[["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
	[['x', 'o', 'x'], ['-', 'o', 'o'], ['i', 'o', 'o']],
	[['o', 'o', 'x'], ['-', 'o', 'o'], ['i', '-', 'o']],
	[['x', 'o', 'x'], ['-', 'x', 'o'], ['x', 'o', 'o']]
]
for spielstand in spielstande:
	if sieg_drl(spielstand):
		print('sieg')
		print(spielstand)
	else:
		print('kein sieg')


# Schreibe eine Funktion, die überprüft,
# ob ein gegebener Text ein Palindrom ist
# (d.h., vorwärts und rückwärts gelesen dasselbe ist

def check_palindrom(word):
	drow = ""
	word = word.lower()
	for buchstabe in range(len(word)):
		word[len(word) - 1]
		drow += word[len(word) - 1 - buchstabe]
	return drow == word


print(check_palindrom("anhna"))


def check_palindrom2(word):
	for b in range(len(word)):
		if word[b] != word[-1 - b]:
			return False
	return True


print(check_palindrom2('anhna'))

#  Alte Loesungen


# Schreibe eine Funktion, die den Durchschnitt einer Liste von Zahlen berechnet
zahlen = [10, 20, 30, 40, 50]


def get_durchschnitt(liste):
	summe = 0
	zaehler = 0
	for x in liste:
		summe += x
		zaehler += 1
	durchschnitt = summe / zaehler
	return durchschnitt


# Mit Python functions
# def get_durchschnitt(liste):
# 	return sum(liste) / len(liste)
print(get_durchschnitt(zahlen))

# Schreibe eine Funktion, die eine Liste von Zahlen nimmt
# und eine neue Liste mit den Quadraten dieser Zahlen zurückgibt
zahlen = [2, 4, 6, 8, 10]  # -> # Sollte [4, 16, 36, 64, 100] ergeben


def liste_to_quadrat_liste(liste):
	quadrat_liste = []
	for zahl in liste:
		quadrat_liste.append(zahl ** 2)
	return quadrat_liste


print(liste_to_quadrat_liste(zahlen))


# Schreibe eine Funktion,
# die das Maximum und das Minimum aus einer
# Liste von Zahlen zurückgibt. (wenn es geht ohne min() und max())
# return [ min ,max]
# def min_max_liste(liste):
# 	min_wert = min(liste)
# 	max_wert = max(liste)
# 	return [min_wert, max_wert]

def min_max_liste(liste):
	min_wert = liste[0]
	max_wert = liste[0]
	for zahl in liste:
		if min_wert > zahl:
			min_wert = zahl
		if max_wert < zahl:
			max_wert = zahl
	return [min_wert, max_wert]


print(min_max_liste(zahlen))

# Schreibe die Funktionen zur Überprüfung der Sieg bedingungen des Tic Tac Toe spiels.
# Sie sollen True zurückgeben bei einem Sieg und False wenn sie nicht erfüllt werden
# waagerechter Sieg
spielfeld = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


def sieg_waage(nested_list):
	for liste in nested_list:
		if liste[0] == liste[1] and liste[0] == liste[2] and liste[0] != '-':
			return True
	return False


# [x, x, x]
# [-, o, o]
# [o, -, o]

spielfeld = [['x', True, 'x'], [True, True, 'x'], [True, True, 'x']]


# senkrechter Sieg
def sieg_senk(nested_list):
	for x in range(3):
		if nested_list[0][x] == nested_list[1][x] == nested_list[2][x] != '-':
			return True
	return False


def sieg_diag_ol_ur(nested_list):
	if nested_list[0][0] == nested_list[1][1] == nested_list[2][2] and nested_list[0][2] != "-":
		return True
	else:
		return False


def sieg_diag_or_ul(nested_list):
	if nested_list[0][2] == nested_list[1][1] == nested_list[2][0] and nested_list[0][2] != "-":
		return True
	else:
		return False


spielfeld = [['o', '-', 'o'], ['o', '', '-'], ['o', 'o', 'o']]
for x in spielfeld:
	print(x)
print(sieg_waage(spielfeld))
print(sieg_senk(spielfeld))
print(sieg_diag_ol_ur(spielfeld))
print(sieg_diag_or_ul(spielfeld))

# Schreibe eine Funktion, die überprüft,
# ob ein gegebener Text ein Palindrom ist
# (d.h., vorwärts und rückwärts gelesen dasselbe ist

# def palindrom(string):
# 	for x in range(len(string)//2):
# 		if pal[x] == pal[len(string)-1-x]:
# 			continue
# 		else:
# 			return False
# 	return True
pal = 'Erika feuert nur untreue Fakire'.replace(' ', '')
# def palindrom(string):
# 	re_string = string[::-1]
# 	print(re_string)
# 	# for x in string:
# 	# 	re_string = x + re_string
# 	if re_string.upper() == string.upper():
# 		return True
# 	else:
# 		return False
# print('###################################################')
# print(palindrom(pal))
