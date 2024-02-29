range(10)  # mindestens 1 max 3 Argumenten start , stop , schrittweite

zahlenreihenfolge = list(range(10))  # Bei 1. Argument gibt man nur den stop-wert an -> Zahlenreihenfolge von 0 - 9
print(zahlenreihenfolge)

zahlenreihenfolge = list(range(2, 100))  # Bei 2. Argumenten start und stop -> 2 -99
print(zahlenreihenfolge)

zahlenreihenfolge = list(range(2, 11, 2))  # Bei 3. Argumenten start stop und schrittweite -> 2, 4, 6, 8, 10
print(zahlenreihenfolge)

cd = list(range(10, -1, -1))  # Es können auch negative Argumente übergeben werden um Rückwärts zu Zählen
print(cd)

for x in range(10):
	print(x)

# for (cd == 10 ; cd < 0 ; cd --){
# Schleifenkörper
# }

for cd in range(10, -1, -1):
	if cd == 0:
		print('Happy new year')
	else:
		print(cd)
z = 0
for x in range(101):
	if x % 5 == 0:
		z += 1
print(z)

summe = 0
for x in range(1,1000):
	summe += x
print(summe)

körner = 1
for feld in range(1,65):
	körner = körner * 2
print(körner)
print(2**64)
