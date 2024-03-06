user = ['Bob', 'Eve', 'Jim', 'John', 'Tim']
# printe für alle Namen der Liste user "createuser username"
# Beispiel "createuser Bob"
for name in user:
    print(f'createuser {name}')

# Wandele die Username in lowercase um bevor du sie ausdruckst
# Beispiel "createuser bob"
for name in user:
    print(f'createuser {name.lower()}')

# Erweitere die Ausgabe um einen Zähler
# Beispiel "createuser Bob 1"
# Beispiel "createuser Eve 2"


for index, name in enumerate(user, 1):
    print(f'createuser {name} {index}')

# Es sollen nur noch User ausgegeben werden die ein "i"" in ihrem namen haben.
for name in user:
    if 'i' in name:
        print(name)

for name in user:
    for letter in name:
        if letter == "i":
            print(name)
# Tausche in jedem Namen den Buchstaben "B" gegen ein '8', 'E' gegen ein '3' 'o' gegen 0 und 'i' gegen '1' aus.
for name in user:
    print(name.replace('B', '8').replace('E', '3').replace('o', '0').replace('i', '1'))

# Es soll folgende Ausgabe mit einer Schleife erzeugt werden
# Tip "\t"

# Bob
# 	 Eve
# 		 Jim
# 			 John
# 				 Tim
for z, name in enumerate(user):
    print("\t" * z, name)

rand_zahlen = [452, 30, 688, 177, 534, 137, 490, 387, 845, 882, 896, 798, 456, 691, 932, 978, 333, 499, 222, 775, 866,
               976, 809, 803, 970, 840, 2, 814, 638, 189, 255, 960, 199, 350, 365, 104, 396, 794, 489, 497, 380, 598,
               609, 987, 328, 314, 678, 331, 85, 426, 31, 58, 540, 124, 8, 454, 979, 744, 280, 584, 323, 665, 627, 999,
               244, 31, 764, 420, 797, 534, 121, 655, 427, 758, 131, 652, 440, 571, 408, 154, 138, 70, 798, 325, 584,
               718, 923, 398, 285, 342, 392, 206, 863, 266, 832, 746, 906, 180, 172, 183, 224, 207, 800, 349, 786, 554,
               305, 52, 871, 161, 364, 542, 944, 739, 1001, 154, 771, 732, 957, 590, 444, 870, 527, 394, 426, 199, 129,
               634,
               897, 899, 407, 334, 372, 489, 498, 913, 255, 684, 813, 231, 710, 628, 578, 331, 680, 468, 111, 595, 720,
               320, 650, 667, 635, 589, 408, 41, 770, 153, 697, 506, 573, 931, 678, 292, 915, 197, 926, 991, 937, 185,
               816, 587, 555, 341, 767, 261, 930, 950, 879, 100, 521, 853, 441, 650, 429, 196, 703, 228, 911, 902, 16,
               518, 143, 528, 106, 806, 230, 82, 548, 476, 736]

# Elemente addieren: Gehe durch die Liste rand_zahlen und addiere alle Elemente [Summe]
print(sum(rand_zahlen))
summe = 0
for zahl in rand_zahlen:
    summe += zahl
print(summe)

# Gib die Anzahl der Elemente aus ohne len oder andere eingebaute Funktionen
print(len(rand_zahlen))
i = 0
for zahl in rand_zahlen:
    i += 1
print(i)

# Größtes Element finden: Finde das größte Element in einer Liste von Zahlen.
g = rand_zahlen[0]
for zahl in rand_zahlen:
    if zahl > g:
        g = zahl
print(g)
print(max(rand_zahlen))
# Ausgabe aller Elemente *2
for zahl in rand_zahlen:
    print(zahl * 2)

# Nur Gerade Zahlen Ausgeben
for i in rand_zahlen:
    if i % 2 == 0:
        print(i)

# Gebe nur Zahlen aus die zwischen 150 und 300 sind.
print('________________________________________________')
for i in rand_zahlen:
    if 150 < i < 300:
        print(i)
# Füge alle Zahlen die kleiner als 100 sind in eine Liste kleiner100 hinzu.
kleiner = []
for i in rand_zahlen:
    if i < 100:
        kleiner.append(i)

print(kleiner)

# Sortiere alle Zahlen aus der rand_zahlen in eine nested_list
# nested_list = [[Zahlen 0-300],[Zahlen 301 - 600], [Zahlen 601-999]]
nested_list = [[], [], []]
for i in rand_zahlen:
    if 0 <= i <= 300:
        nested_list[0].append(i)
    elif 301 <= i <= 600:
        nested_list[1].append(i)
    elif 601 <= i <= 999:
        nested_list[2].append(i)

print(nested_list)

mem_mom = [33, 44, 40, 52, 60, 56, 40, 52, 60, 56]

# Info: Mittelwert = Summe / Anzahl

# Berechne den Mittelwert aller Daten "Gesamt"


# Berechne den Mittelwert der ersten 5 Einträge "Vormittag"


# Berechne den Mittelwert der letzten 5 "Nachmittag"


# Gib die Mittel werte in der Konsole aus
# 1. Der gesamte Mittelwert
# 2. Der größere Mittelwert. Wenn Vormittag und Nachmittag gleich sind dann zuesr Vormittag
# Beispiel
# Gesamt 49
# Nachmittag 51
# Vormittag 48


# --------------------------------
muster = [1, 2, 3, 4, 5]
# gib mithilfe der Liste muster das Muster aus


# 1   2   3   4   5
# 2   4   6   8  10
# 3   6   9  12  15
# 4   8  12  16  20
# 5  10  15  20  25
