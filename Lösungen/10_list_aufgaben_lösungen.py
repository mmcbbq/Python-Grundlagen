# Erstelle eine Liste super_liste mit folgenden Items: 20, 50.5 , 'Hallo', True, 'Löschen' , 'auf Wiedersehen'
super_liste = [20, 50.5, 'Hallo', True, 'Löschen', 'auf Wiedersehen']
# Ändere den Wert des ersten Elementes zu 95
super_liste[0] = 95
# Kopiere den Wert des 4 Items auf den 2 index
super_liste[2] = super_liste[3]
# Ändere das 4 Element zu False
super_liste[3] = False
# Füge das Element "999" an der letzten Stelle der Liste an
super_liste.append("999")
# Füge das Element "Nummer 5" an der 5 Stelle ein
super_liste.insert(4, 'Nummer 5')
# tauche das Element mit dem Index 0 und das Index 5
super_liste[0], super_liste[5] = super_liste[5], super_liste[0]
# Schreibe eine If anweisung die das Element 'bin da' löscht, wenn es vorhanden ist.
# Wenn das Element nicht vorhanden ist, soll es an letzter Stelle hinzugefügt werden
if 'bin da' in super_liste:
	super_liste.remove('bin da')
else:
	super_liste.append('bin da')
# copy die liste in die Variable list_copy
list_copy = super_liste.copy()
# Leere die Originalliste
super_liste.clear()
# Füge die letzten 3 Elemente der list_copy an die super_liste an.
super_liste.extend(list_copy[-3:0])

# Erstellen Sie eine Liste von 5 Städten, die Sie besuchen möchten.
# Fügen Sie dann eine weitere Stadt hinzu und entfernen Sie die dritte Stadt aus der Liste.
# Schließlich geben Sie die Liste der verbleibenden Städte aus.
city = ['Paris', 'Kyoto', 'Venedig', 'Sydney', 'New York City']
city.append('Hamburg')
city.pop(2)
# Schreibe den IHK_Prüfung Programm um. Verwende anstatt Variablen für die Punkte ein Liste
# ap1 = 50
# ap2_doku = 50
# ap2_praesi = 50
# ap2_1 = 50
# ap2_2 = 50
# ap2_wiso = 50

