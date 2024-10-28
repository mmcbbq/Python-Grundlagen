# Erstellen Sie eine Liste von 5 Städten, die Sie besuchen möchten.
# Fügen Sie dann eine weitere Stadt hinzu und entfernen Sie die dritte Stadt aus der Liste.
# Schließlich geben Sie die Liste der verbleibenden Städte aus.


# Erstelle eine Liste super_liste mit folgenden Items: 20, 50.5, 'Hallo', True, 'Löschen', 'auf Wiedersehen'

# Ändere den Wert des ersten Elementes zu 95

# Kopiere den Wert des 4 Items auf den 2 index

# Ändere das 4 Element zu False

# Füge das Element "999" an der letzten Stelle der Liste an

# Füge das Element "Nummer 5" an der 5 Stelle ein

# tauche das Element mit dem Index 0 und das Index 5

# Schreibe eine If anweisung die das Element 'bin da' löscht, wenn es vorhanden ist.
# Wenn das Element nicht vorhanden ist, soll es an letzter Stelle hinzugefügt werden

# copy die liste in die Variable list_copy

# Leere die Originalliste

# Füge die letzten 3 Elemente der list_copy an die super_liste an.

import inspect

zahl1 = 12
zahl2 = zahl1

array1 = [1,2,3]
array2 = array1
print(inspect.getmembers(array1))


nummber = 349872390486783459067823459086

print('1nr Stelle\t\t', nummber % 10)
print('10nr Stelle\t\t', nummber % 100 // 10)
print('100nr Stelle\t', nummber % 1000 // 100)
print('1000nr Stelle\t', nummber % 10000 // 1000)
print('10000nr Stelle\t', nummber % 100000 // 10000)

div = 10
while True:
	print(f"{div // 10} Stelle", nummber % div // (div // 10))
	div *= 10
	if nummber % div == nummber:
		break
