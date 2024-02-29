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

