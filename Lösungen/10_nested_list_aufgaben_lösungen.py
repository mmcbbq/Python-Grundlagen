# Erstelle eine list tic
tic = []
# Füge tic eine Liste mit den werten 'l','l','l' hinzu
# Füge tic eine 2. liste mir den werten 'k','k','k' hinzu
# Füge tic eine 3. liste mir den werten 'b','b','b' hinzu
tic.append(['l', 'l', 'l'])
tic.append(['k', 'k', 'k'])
tic.append(['b', 'b', 'b'])
# Printe jede unterliste in einer Zeile aus
print(tic[0])
print(tic[1])
print(tic[2])
# ['l', 'l', 'l']
# ['k', 'k', 'k']
# ['b', 'b', 'b']
# ändere die liste wie folgt ab
# ['x', 'l', 'l']
# ['k', 'x', 'k']
# ['b', 'b', 'x']
tic[0][0] = 'x'
tic[1][1] = 'x'
tic[2][2] = 'x'
print(tic[0])
print(tic[1])
print(tic[2])
print('---------------------------------------')

# ändere die liste wie folgt ab
# ['x', 'o', 'o']
# ['x', 'x', 'o']
# ['o', 'x', 'o']
tic[0][1] = 'o'
tic[0][-1] = 'o'
tic[1][0] = 'x'
tic[1][-1] = 'o'
tic[-1][0] = 'o'
tic[-1][1] = 'x'
tic[-1][-1] = 'o'
print(tic[0])
print(tic[1])
print(tic[2])
print('---------------------------------------')

# ändere die liste wie folgt ab
# ['o', 'o', 'o']
# ['x', 'x', 'o']
# ['o', 'x', 'o']
tic[0][0] = 'o'
print(tic[0])
print(tic[1])
print(tic[2])
print('---------------------------------------')

# schriebe ein Programm das 2 Zahlen von 1 bis 3 und einem Buchstaben vom user fordert
# Anschliessend soll der Wert mit der Pos den zwei Zahlen mit den Buchstaben überschrieben werden
# und die Liste wie in der vorherigen Aufgabe ausgegeben werden
x_wert = int(input('x wert 1-3'))
y_wert = int(input('y wert 1-3'))
zeichen = input('Zeichen')
# 3['o', 'o', 'o']
# 2['x', 'x', 'o']
# 1['o', 'x', 'o']
#    1    2    3
if 0 < y_wert <= 3 and 0 < x_wert <= 3:
	tic[y_wert - 1][x_wert - 1] = zeichen
	print(tic[2])
	print(tic[1])
	print(tic[0])
else:
	print('Falsche Eingabe')
# Beispiel Zahl1 = 3 Zahl2 = 2 Buchstabe = p
# 3['o', 'o', 'o']
# 2['x', 'x', 'p']
# 1['o', 'x', 'o']

# Zähle alle "o" in der mittleren Liste1
if tic[0].count('o') == 3:
	print('Sieg')
# Schreib eine If anweisung die 'Sieg' ausgibt wenn das Zeichen auf pos 1.1 das selbe ist wie auf pos 2.2 und 3.3

if tic[0][0] == tic[1][1] and tic[0][0] == tic[2][2]:
	print('Sieg')
