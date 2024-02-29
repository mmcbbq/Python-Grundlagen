# Zahlen addieren:
# Schreibe eine While-Schleife,
# die die Summe von Zahlen von 1 bis zu einer vom Benutzer
# eingegebenen Zahl berechnet.
summe = 0
z = 0
ende = int(input('Summe Zahl'))
while z < ende:
	z += 1
	summe += z
print(summe)

# Passwort überprüfen:
# Erstelle eine Schleife,
# die den Benutzer nach einem Passwort fragt,
# bis das korrekte Passwort eingegeben wird.
password = 'G3h31m'
# ant = input('Password')
# while ant != password:
# 	ant = input('Password wiederholen')
# print('ich bin drin')
pass_check = True
versuche = 0
while pass_check:
	if versuche == 3:
		print('Das war zu viel')
		break
	ant = input('Password')
	if password == ant:
		pass_check = False
	else:
		versuche += 1
		print('Das war Falsch nochmal')
print('Du bist drin')




# Ein Spieler soll eine (zufällig gewählte) Zahl zwischen 1 und 100 erraten.
# Das Programm soll jeweils die Meldungen „Die Zahl ist zu groß“,
# „Die Zahl ist zu klein“ bzw.
# „Treffer“ ausgeben.
# Wenn die Zahl zu Gross oder zu klein ist soll die Frage erneut gestellt werden

import random
zufall_zahl = random.randint(1, 100)
print(zufall_zahl)
versuche = 10
nicht_richtig = True

while nicht_richtig:

	ant = int(input('Zahl zwischen 1 -100'))
	if ant < zufall_zahl:
		print('Zu klein')
	elif ant > zufall_zahl:
		print('zu Groß')
	elif ant == zufall_zahl:
		print('Treffer')
		nicht_richtig = False
	versuche -= 1
	if versuche == 0:
		print('Keine Versuche mehr')
		break
	print('Du hast noch ',versuche)


print('Die Zahl war ', zufall_zahl)



