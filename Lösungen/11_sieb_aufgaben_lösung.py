# Das Sieb des Eratosthenes ist ein Algorithmus zur Bestimmung einer Liste oder Tabelle
# aller Primzahlen kleiner oder gleich einer vorgegebenen Zahl.

# Aus http://de.wikipedia.org/wiki/Sieb_des_Eratosthenes:

# Zunächst werden alle Zahlen 2, 3, 4, … bis zu einem frei wählbaren Maximalwert N aufgeschrieben.
# Die zunächst unmarkierten Zahlen sind potentielle Primzahlen.
# Die kleinste unmarkierte Zahl ist immer eine Primzahl.
# Nachdem eine Primzahl gefunden wurde, werden alle Vielfachen dieser Primzahl als zusammengesetzt markiert.
# Man bestimmt die nächstgrössere nicht markierte Zahl.
# Da sie kein Vielfaches von Zahlen kleiner als sie selbst ist (sonst wäre sie markiert worden),
# kann sie nur durch eins und sich selbst teilbar sein.
# Folglich muss es sich um eine Primzahl handeln.
# Diese wird dementsprechend als Primzahl ausgegeben.
# Man streicht wieder alle Vielfachen und führt das Verfahren fort,
# bis man am Ende der Liste angekommen ist.
# Im Verlauf, des Verfahren werden alle Primzahlen ausgegeben.
import timeit

start = timeit.default_timer()

# primzahlen_kandidaten = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
# 						 28, 29, 30, 31,
# 						 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,
# 						 56, 57, 58, 59,
# 						 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
# 						 84, 85, 86, 87,
# 						 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
primzahlen_kandidaten = []
for x in range(2, 101):
    primzahlen_kandidaten.append(x)

for primzahl in primzahlen_kandidaten:
    if primzahl == len(primzahlen_kandidaten) ** (1 / 2):
        break
    for kandidaten in primzahlen_kandidaten:
        if kandidaten % primzahl == 0 and kandidaten != primzahl:
            primzahlen_kandidaten.remove(kandidaten)
print(len(primzahlen_kandidaten))
print(primzahlen_kandidaten)

stop = timeit.default_timer()

print('Time: ', stop - start)

import matplotlib.pyplot as plt
import numpy as np

tiere = ('Katzen', 'Hunde', 'Kleintiere', 'Ziervögel')
anzahl = [15.7, 10.7, 5, 3.5]

y_pos = np.arange(len(tiere))

plt.bar(y_pos, anzahl, align='center')
plt.xticks(y_pos, tiere)
plt.ylabel('Anzahl in Millionen')
plt.title('Haustiere in Deutschland (2020)')
# Striche auf x-Achse ausschalten
plt.tick_params(
    axis='x',
    which='both',  # major und minor ticks
    bottom=False  # ticks auf der x-Achse (unten)
)
plt.show()
import timeit
from math import sqrt

start = timeit.default_timer()

primzahl_kandidaten = [True] * 101
primzahl_kandidaten[0], primzahl_kandidaten[1] = False, False
i = 0
for primzahl in range(0, int(sqrt(len(primzahl_kandidaten) + 2))):
	if primzahl_kandidaten[primzahl]:
		for j in range(i * 2, len(primzahl_kandidaten), i):
			primzahl_kandidaten[j] = False
	i += 1
i = 0
print(primzahl_kandidaten)
for x in primzahl_kandidaten:
	if x:
		print(i)
	i += 1

stop = timeit.default_timer()
print(primzahl_kandidaten.count(True))
print('Time: ', stop - start)

