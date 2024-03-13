# Heron von Alexandria (genannt Mechanicus) war ein Mathematiker und Ingenieur,
# der vermutlich im 1. Jahrhundert lebte. Bekannt sind vor allem seine Ausführungen zu automatischen,
# teilweise sogar schon programmierbaren Geräten und der Ausnutzung von Wasser,
# Luft und Hitze als treibende Kraft. Hier sind insbesondere die Erfindung der Aeolipile,
# auch Heronsball genannt, und der Heronsbrunnen zu nennen (wikipedia).
#
# Außerdem entwickelte er einen Algorithmus, mit dem man für eine beliebige Zahl
# die Quadratwurzel auf eine beliebige Genauigkeit berechnen kann … das Heron-Verfahren:
#
# Wähle eine Startwert x zur Bestimmung der Wurzel aus w.
# Wähle
#
# x = (x + w/x)/2
#
# Wiederhole  mit den jeweils neuen Näherungswerten x bis die gewünschte Genauigkeit erreicht ist.
# Die Grundidee für dieses Verfahren basiert auf der Frage, wie ein Rechteck in ein flächengleiches Quadrat
# umgewandelt werden kann … dafür wird die Seitenlänge des Quadrats benötigt.

# Schreibe den Algorithmus in Pyhton fuer 10 wiederholungen

# Schreibe eine while loop die den Algorithmus solange ausfuehrt
# bis der Näherungswert auf 0.1 des exakten Ergebnis liegt


### Sieb des Eratosthenes

# Das Sieb des Eratosthenes ist ein Algorithmus zur Bestimmung einer Liste oder Tabelle aller Primzahlen
# kleiner oder gleich einer vorgegebenen Zahl.
#
# Aus http://de.wikipedia.org/wiki/Sieb_des_Eratosthenes:
#
# Zunächst werden alle Zahlen 2, 3, 4, … bis zu einem frei wählbaren Maximalwert N aufgeschrieben.
# Die zunächst unmarkierten Zahlen sind potentielle Primzahlen. Die kleinste unmarkierte Zahl ist immer eine Primzahl.
# Nachdem eine Primzahl gefunden wurde, werden alle Vielfachen dieser Primzahl als zusammengesetzt markiert.
# Man bestimmt die nächstgrössere nicht markierte Zahl.
# Da sie kein Vielfaches von Zahlen kleiner als sie selbst ist (sonst wäre sie markiert worden),
# kann sie nur durch eins und sich selbst teilbar sein. Folglich muss es sich um eine Primzahl handeln.
# Diese wird dementsprechend als Primzahl ausgegeben. Man streicht wieder alle Vielfachen und führt das Verfahren fort,
# bis man am Ende der Liste angekommen ist. Im Verlauf des Verfahren werden alle Primzahlen ausgegeben.
