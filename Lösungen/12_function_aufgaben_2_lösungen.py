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
spielfeld = [[True, True, True], [True, True, True], [True, True, True]]


def sieg_waage(nested_list):
	for liste in nested_list:
		if type(liste[0]) is bool:
			continue
		elif liste[0] == liste[1] and liste[0] == liste[2]:
			return True
	return False


# [x, x, x]
# [-, o, o]
# [o, -, o]

spielfeld = [['x', True, 'x'], [True, True, 'x'], [True, True, 'x']]


# senkrechter Sieg
def sieg_senk(nested_list):
	for x in range(3):
		if type(nested_list[0][x]) is bool:
			continue
		elif nested_list[0][x] == nested_list[1][x] == nested_list[2][x]:
			return True
	return False





# [x, x, o]
# [-, o, o]
# [o, -, o]

# diagonaler Sieg oben links nach unten Rechts
# [o, x, x]
# [-, o, o]
# [o, -, o]


def sieg_diag_ol_ur(nested_list):
	if nested_list[0][0] == nested_list[1][1] == nested_list[2][2] and type(nested_list[0][0]) is not bool:
		return True
	else:
		return False

# diagonaler Sieg unten links nach oben Rechts
# [x, x, o]
# [-, o, o]
# [o, -, o]
def sieg_diag_or_ul(nested_list):
	if nested_list[0][2] == nested_list[1][1] == nested_list[2][0] and type(nested_list[0][2]) is not bool:
		return True
	else:
		return False


spielfeld = [[True, True, 'o'], [True, 'o', True], ['o', True, True]]
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
pal = 'Erika feuert nur untreue Fakire'.replace(' ','')
def palindrom(string):
	re_string = string[::-1]
	print(re_string)
	# for x in string:
	# 	re_string = x + re_string
	if re_string.upper() == string.upper():
		return True
	else:
		return False
print('###################################################')
print(palindrom(pal))

