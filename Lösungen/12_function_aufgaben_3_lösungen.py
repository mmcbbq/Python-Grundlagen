# Schreibe eine Funktion, die überprüft, ob eine Zahl zwischen 10 und 20 liegt

def zwischen_10_20(zahl: int) ->bool:
	if zahl >= 10 and zahl <= 20:
		return True
	else:
		return False


print(zwischen_10_20(10))
print(zwischen_10_20(20))
print(zwischen_10_20(9))
print(zwischen_10_20(21))


# Schreibe eine Funktion, die überprüft, ob eine Zahl entweder kleiner als 5 oder größer als 15 ist.
def kleiner_5_groesser_15(zahl:int) -> bool:
	if zahl < 5 or zahl > 15:
		return True
	else:
		return False


print('_______________________________')
print(kleiner_5_groesser_15(4))
print(kleiner_5_groesser_15(16))
print(kleiner_5_groesser_15(5))
print(kleiner_5_groesser_15(15))


# Eine Funktion mit 2 Parametern die überprüft ob genau eine True ist.
def xor_true(bool_1: bool, bool_2: bool) -> bool:
	return bool_1 ^ bool_2


a = True
b = False
print('---------------------------------')
print(xor_true(a, b))
print(xor_true(a, a))
print(xor_true(b, b))
print(xor_true(b, a))


# Schreibe eine Funktion, die überprüft, ob eine Zahl sowohl durch 2 als auch durch 5 teilbar ist.
def teilbar_2_5(zahl:int) ->bool:
	if zahl % 2 == 0 and zahl % 5 == 0:
		return True
	else:
		return False


for x in range(1, 101):
	print(teilbar_2_5(x), x)

# Schreibe eine Funktion mit 3 Parametern par_1 = bool par_2 = bool und par_3 = string
# Der String soll entweder and, or oder xor.
# Die Funktion soll eine Art Logische Operator Taschenrechner werden


def logischer_rechner(par_1, par_2, string):
	if 'and' == string:
		# print(f'{par_1} and {par_2} = {par_1 and par_2}')
		print(par_1, 'and', par_2, '=', par_1 and par_2)
	elif 'or' == string:
		print(f'{par_1} or {par_2} = {par_1 or par_2}')
	elif 'xor' == string and par_1 ^ par_2:
		print(f'{par_1} xor {par_2} = {par_1 ^ par_2}')


print('--------------------------------')
logischer_rechner(False, False, 'and')
logischer_rechner(True, False, 'or')
logischer_rechner(True, False, 'xor')
logischer_rechner(True, True, 'test')

# True True and  -> Ausgabe True
# True True or  -> Ausgabe True
# True True xor  -> Ausgabe False
