import math


# Schreibe eine Funktion zur Berechnung der Fläche eines Quadrates
def quadrat_flaech(a: int) -> int:
	flache = a * a
	return flache


# Schreibe eine Funktion zur Berechnung der Fläche eines Rechteckes
def rechteck_area(a: int, b: int) -> int:
	area = a * b
	return area


# Schreibe eine Funktion zur Berechnung der Fläche eines Kreises
def kreis_area_mit_radius(r: int) ->int:
	area = math.pi * r ** 2
	return area


def kreis_area_mit_durch(d: int) -> int:
	area = math.pi * d ** 2 / 4
	return area


# Schreibe eine Funktion die 2 Zahlen als übergabe Parameter bekommt und die größere Zahl wieder gibt
def bigger(zahl1: int, zahl2: int) -> int:
	if zahl1 > zahl2:
		return zahl1
	elif zahl1 < zahl2:
		return zahl2
	else:
		return print('sind gleich')


# Schreibe eine Funktion die überprüft, ob eine Zahl positiv negativ oder null ist.
def check_zahl(a: int) ->str:
	if a > 0:
		return 'positiv'
	elif a < 0:
		return 'negativ'
	elif a == 0:
		return 'Null'


print(quadrat_flaech(5))
print(rechteck_area(5, 3))
print(kreis_area_mit_radius(5))
print(kreis_area_mit_durch(10))
print(bigger(15, 15))

zahl = 1

print(check_zahl(zahl))
print(check_zahl(rechteck_area(quadrat_flaech(5), 3)))
