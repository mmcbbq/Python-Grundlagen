# Die while-Schleife in Python wird verwendet,
# um einen bestimmten Codeblock so lange auszuführen,
# wie eine bestimmte Bedingung wahr ist.
# Die allgemeine Syntax lautet:
# while Bedingung:
#Code
# Vorsicht vor Endlosen Schleifen !!!!
#
# Es ist wichtig, sicherzustellen,
# dass die Bedingung in der while-Schleife irgendwann False wird.
# Andernfalls wird die Schleife endlos weiterlaufen,
# was zu einem Programmabsturz oder einer schlechten Leistung führen kann
while True:
    print('Endlose Schleife')

# while mit Zähler
n = 10
while n > 0:  # Schleife läuft solange True
    print(n)
    n -= 1

ant = input('Soll das Programm geschlossen werden? y n')

while ant != 'y':
    print('Funktion')
    ant = input('Soll das Programm geschlossen werden? y n')

# break -> stop die Schleife
x = 50
while x > 0:
    x -= 1
    print(x)

    if x == 25:
        break

# continue stop den Schleifendurchlauf und springt in den den Schleifenkopf
print('continue Schleife')
while x > 0:
    x -= 1
    if x == 10:
        continue
    print(x)

my_liste = ['Bob', 'Tim', 'Tom', 'Eve', ]
x = 0
name = my_liste[x]

while name != 'Tom':
    print('Kein Treffer')
    x += 1
    name = my_liste[x]
print(name, 'hat den index', x)
