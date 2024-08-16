# # Der User wird nach einer Zahl gefragt und es soll ausgegeben werden ob die Zahl = < oder > 10
nummer = int(input('gibt Zahl'))

if nummer == 10:
	print('ist gleich 10')
elif nummer > 10:
	print('ist größer')
elif nummer < 10:
	print('ist kleiner')
#
# # Der User wird nach einer Zahl gefragt. Es soll geprüft werden ob es eine gerade oder ungerade Zahl ist
nummer = int(input('gibt Zahl'))

if nummer % 2 == 0:
	print('ist gerade')
elif nummer % 2 != 0:
	print('ist ungerade')
# Schreibe ein Programm, das den Benutzer nach einem Passwort fragt und prüft, ob es mindestens 8 Zeichen lang ist.
a = input('pass')
if len(a) >= 8:
	print('ist lang')
else:
	print('zu kurz')
# Der User wird nach einer Zahl zwischen 1-7 gefragt
# 1 Montag 2 Dienstag 3 Mittwoch 4 Donnerstag 5 Freitag 6 Samstag 7 Sonntag
# Bei anderen eingaben "keine gültige Eingabe"
tag = input('1-7')
if tag == '1':
    print('Montag')
elif tag == '2':
    print('dienstag')
elif tag == '3':
    print('Mi')
elif tag == '5':
    print('Fr')
elif tag == '6':
    print('Sa')
elif tag == '7':
    print('So')
elif tag == '4':
    print('Do')
else:
    print('fehler')

# Der User wird nach seiner Punktzahl gefragt
# sehr gut 100 - 92
# gut       91 - 81
# befriedigend 80 - 67
# ausreichend 66 - 50
# mangelhaft 49 - 30
# ungenügend 29 - 0
# Bei anderen eingaben "keine gültige Eingabe"


punkte = int(input('Deine Punktzahl'))

if punkte > 100:
    print('falsche')
elif punkte >= 92:
    print('1')
elif punkte >= 81:
    print('gut')
elif punkte >= 67:
    print('3')
elif punkte >= 50:
    print('4')
elif punkte >= 30:
    print('5')
elif punkte >= 0:
    print('6')
else:
    print('keine ...')