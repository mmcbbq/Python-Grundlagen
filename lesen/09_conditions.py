# # Frage dem User nach seinem Alter
alter = int(input("Wie alt bist du?"))  # Zeigt den string "Wie alt bist du" in der Console an und erwartet eine Antwort
#
# Überprüfen ob der User mindestens 18 ist
if alter >= 18:  # Wenn der Wert der Varaible alter größer gleich 18 ist
	print("Hallo")  # Dann sag Hallo. Der ganze Code Block der eingerückt ist wird ausgeführt
elif alter >= 16:  # ansonsten wenn. Eine weitere Überprüfung die ausgeführt wird wenn die Bedingung True ist
	print('Hallo du brauchst eine Begleitung')
# Es wird immer nur der Code einer Bedingung Ausgeführt
else:  # "Sonst" Wenn keine bedingung True ist, wird der else Block ausgeführt
	print('Du bist zu jung')

# If Anweisungen können auch verschachtelt werden.

alter = int(input('Wie alt'))
geschlecht = input('Geschlecht')

if alter >= 18:
	if geschlecht == 'm':
		print('Hallo Herr', end=' ')
	elif geschlecht == 'w':
		print('Hallo Frau', end=' ')
		print('du bist gefeuert')
	else:
		print("Falsche Eingabe")
else:
	print('du bist nicht')

zahl1 = int(input('zahl1'))
zahl2 = int(input('zahl2'))
zahl3 = int(input('zahl3'))

if zahl1 > zahl2:
	if zahl1 > zahl3:
		print('zahl1 ist die größte')
	else:
		print('zahl3 ist die größte')
elif zahl2 > zahl3:
	print('zahl2 ist die größte')
else:
	print('zahl3 ist die größte')

if zahl1 > zahl2 and zahl1 > zahl3:
	print('zahl1')
elif zahl2 > zahl1 and zahl2 > zahl3:
	print("zahl2")
elif zahl3 > zahl1 and zahl3 > zahl2:
	print("zahl3")

# empty String
print('empty String')
if '':
	print('True')
else:
	print(False)

print('String')

if 'Voll':
	print('True')
else:
	print('False')

# int
print('1 as int')

if 1:
	print('True')
else:
	print('False')

print('0 as int')

if 0:
	print('True')
else:
	print('False')

print('123 as int')

if 123:
	print('True')
else:
	print('False')

print('0. as float')

if 0.:
	print('True')
else:
	print('False')
print('1. as float')

if 1.:
	print('True')
else:
	print('False')
print('1522.125 as float')

if 1522.12:
	print('True')
else:
	print('False')


