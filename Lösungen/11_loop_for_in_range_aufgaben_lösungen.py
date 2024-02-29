# Berechne die Summe aller Zahlen von 1 - 500
print('Aufgabe 1')
summe = 0
for i in range(1, 501):
	summe += i
print(summe)
# Schreib eine Schleife die folgendes Muster ausgibt
# *
# **
# ***
# ****
# *****
print('Aufgabe 2')
print('#######################')

for i in range(1, 6):
	print('*' * i)
# Schreib eine Schleife die folgendes Muster ausgibt
# *****
# ****
# ***
# **
# *
print('Aufgabe 3')
print('#######################')
for i in range(5, 0, -1):
	print('*' * i)

# Schreib eine Schleife, die folgendes Muster ausgibt
# 1
# 12
# 123
# 1234
# 12345
print('Aufgabe 4')
print('#######################')
for zeile in range(1, 6):
	for spalte in range(1, zeile + 1):
		print(spalte, end='')
	print()

# Schreib eine Schleife, die folgendes Muster ausgibt
# 5
# 45
# 345
# 2345
# 12345
print('Aufgabe 5')
print('#######################')

for zeile in range(5, 0, -1):
	for spalte in range(zeile, 6):
		print(str(spalte), end='')
	print()
# Schreib eine Schleife, die folgendes Muster ausgibt
# 12345
# 1234
# 123
# 12
# 1
print('Aufgabe 6')
print('#######################')

for zeile in range(5, 0, -1):
	for spalte in range(1, zeile + 1):
		print(str(spalte), end='')
	print()
# Der user soll zwei Zahlen angeben.
# Bei der Eingabe von 6 und 2 soll folgendes Muster ausgegeben werden
#
print('Aufgabe 7')
print('#######################')
# zahl_1 = int(input('zahl 1'))
# zahl_2 = int(input('zahl 2'))
zahl_1 = 7
zahl_2 = 4

for zahl in range(0, zahl_1):
	print('*' * zahl_2)

#     **
#     **
#     **
#     **
#     **
#     **
for zahl in range(0, zahl_2):
	print('*' * zahl_1)
#     ******
#     ******
for zahl in range(0, zahl_1 + 1):
	print('*' * zahl)
#     *
#     **
#     ***
#     ****
#     *****
#     ******
#
for stern in range(0, zahl_2):
	print('*' * (zahl_1 - stern))

#     ******
#     *****
#
# Bei
# 7
# und
# 4
#
# ****
# ****
# ****
# ****
# ****
# ****
# ****
#
# *******
# *******
# *******
# *******
#
# *
# **
# ***
# ****
# *****
# ******
# *******
#
# *******
# ******
# *****
# ****


# ### fizzbuzz
# Schreiben Sie ein Programm, das die Zahlen von 1 bis 100 ausgibt.
# Bei jeder Zahl, die durch 5 teilbar ist, soll "fizz" ausgegeben werden
# und bei jeder Zahl, die durch 7 teilbar ist,
# soll "buzz" ausgegeben werden.
# Wenn die Zahl sowohl durch 7 als auch durch 5 teilbar ist,
# soll "fizzbuzz" ausgegeben werden.
# Der Modulo-Operator ermittelt den Rest bei Division.
# Somit ist eine Teilbarkeit einfach dann erreicht,
# wenn die Modulo-Operation (%, MOD) den Rest 0 liefert.
print('Aufgabe 7')
print('#######################')

for zahl in range(1, 101):
	if zahl % 5 == 0 and zahl % 7 == 0:
		print('fizzbuzz')
	elif zahl % 5 == 0:
		print('fizz')
	elif zahl % 7 == 0:
		print('buzz')
	else:
		print(zahl)

print('Aufgabe 8')
print('#######################')
for zeile in range(8):
	for zeichen in range(8):
		if (zeichen + zeile) % 2 == 0:
			print('X', end='')
		else:
			print('0', end='')
	print()

# Schreib eine Schleife, die folgendes Muster ausgibt
# OXOXOXOX
# XOXOXOXO
# OXOXOXOX
# XOXOXOXO
# OXOXOXOX
# XOXOXOXO
# OXOXOXOX
# XOXOXOXO
