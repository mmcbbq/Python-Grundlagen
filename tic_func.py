def ask_spieler():
	zahl1 = int(input("Zeile"))
	zahl2 = int(input("Spalte"))
	return zahl1 - 1, zahl2 - 1


def setzte_feld(feld, spieler):
	zug = ask_spieler()
	while check_feld(feld[zug[0]][zug[1]]):
		print("Feld belegt")
		zug = ask_spieler()
	feld[zug[0]][zug[1]] = spieler


def check_feld(feld):
	if feld == 'x' or feld == "o":
		return True
	else:
		return False


def print_spielfeld(feld):
	for index, x in enumerate(feld):
		print(f'Zeile {index + 1}', end='\t')
		for y in x:
			print(f'\t{y}', end="")
		print()
	print('Spalte \t\t1 \t2 \t3')