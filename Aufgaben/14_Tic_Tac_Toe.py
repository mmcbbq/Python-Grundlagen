spielfeld = [[True, True, True], [True, True, True], [True, True, True]]



# schriebe ein Programm das 2 Zahlen von 1 bis 3  user fordert
# Anschliessend soll der Wert mit der Pos der zwei Zahlen abwechselnd mit x und o überschrieben werden werden
# und die Liste wie in der vorherigen Aufgabe ausgegeben werden
spieler = 'Spieler 1'
zeichen = 'x'
# code hier
while True:
	print(spieler, ' ist am  Zug')
	print(spielfeld[2])
	print(spielfeld[1])
	print(spielfeld[0])

	erlaubter_zug = False
	while not erlaubter_zug:
		zahl_1 = int(input('x'))
		zahl_2 = int(input('y'))
		if spielfeld[zahl_2 - 1][zahl_1 - 1] == 'x' or spielfeld[zahl_2 - 1][zahl_1 - 1] == 'o':
			print('Feld vergeben')
		else:
			spielfeld[zahl_2 - 1][zahl_1 - 1] = zeichen
			erlaubter_zug = True




	# print(spielfeld[2])
	# print(spielfeld[1])
	# print(spielfeld[0])
	if spieler == 'Spieler 1':
		spieler = 'Spieler 2'
		zeichen = 'o'
	elif spieler == 'Spieler 2':
		spieler = 'Spieler 1'
		zeichen = 'x'

# Das Programm erweitern, dass ein Feld nur von einem Spieler beschrieben werden kann.
# Sollte das Feld belegt sein muss der Spieler erneut Feld auswählen





#    a     b     c
#       |     |
# 3  -  |  -  |  -
#  _____|_____|_____
#       |     |
# 2  -  |  -  |  -
#  _____|_____|_____
#       |     |
# 1  -  |  -  |  -
#       |     |