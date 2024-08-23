# Funktionen die sich selber aufrufen
def plus(n):
	if n == 1:
		return 1
	return n + plus(n - 1)


print(plus(4))


# plus(4) -> 4 + plus(3) beim return wird die funktion plus mit einem veraenderten Argument aufgerufen
# plus(3) -> 3 + plus(2) das Argument geht wird immer kleiner
# plus(2) -> 2 + plus(1) wenn es dann bei 1 angekommen ist
# plus(1)  1 stop es sich selbst aufzurufen und return nur eine 1
# nun koennen  von hinten nach vorne die return values eingesetzt werden

# plus(1) = 1
# plus(2) -> 2 + plus(1) = 2 + 1
# plus(3) -> 3 + plus(2) = 3 + 2 + 1
# plus(4) -> 4 + plus(3) = 4 + 3 + 2 + 1
# der Funktionsaufruf plus 4 return dann  4 + 3 + 2 + 1 = 10

# https://de.wikipedia.org/wiki/Fibonacci-Folge
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)


# Manche Probleme kann man mit Recursiven Funktionen sehr elegant Loesen

# Um Alle Elemente einer Neste List mit 1 Unterebene auszugeben muss man mit Verschatelten schleifen arbeiten

nested_list1 = [1, 2, 3, ['Unterebene', 4, 5, 6, ], 7, 8, 9, ]
for element in nested_list1:
	if type(element) is not list:
		print(element)
	elif type(element) is list:
		for inner_element in element:
			print(inner_element)
print("---------------------------------------")
# Je tiefer die Liste verschachtelt ist deso mehr Schleifen muss man Schreiben
nested_list2 = [1, 2, 3, ['Unterebene', 4, 5, 6, ["unterunterebene", 1, 2, 3]], 7, 8, 9, ]
for element in nested_list2:
	if type(element) is not list:
		print(element)
	elif type(element) is list:
		for inner_element in element:
			if type(inner_element) is not list:
				print(inner_element)
			elif type(inner_element) is list:
				for inner_inner_element in inner_element:
					print(inner_inner_element)

# Fuer jede weiter verschachtelung muss ein weiterer if else Block mit for Schleife angefuegt werden
# Es setzt damit auch voraus das die tiefe der Verschachtelung bekannt ist

# Mir recursive Funktionen laesst sich das Problem loesen in dem man die Funktion
# selbst aufruft, falls eine Liste gefunden wird

print("------------------------------------------------------------")
nested_list3 = [1, 2, 3, ['Unterebene', 4, 5, 6, ["unterunterebene", 1, 2, 3]], 7, 8, 9, ]


def print_nested_list(liste):
	summe = 0
	for x in liste:
		if type(x) is not list:
			print(x)
		elif type(x) is list:
			print_nested_list(x)


print_nested_list(nested_list3)
# Dadurch ist es auch egal wieviele ebenen es gibt
nested_list5 = [
	["String 1", True, 1],
	["String 2", False, 2],
	[
		["String 3", True, 3],
		["String 4", False, 4],
		[
			["String 5", True, 5],
			["String 6", False, 6],
			[
				["String 7", True, 7],
				["String 8", False, 8],
				["String 9", True, 9],
			],
		],
	],
]
print('-----------------------')
print_nested_list(nested_list5)