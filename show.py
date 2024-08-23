geld = {"500": 1, '200': 0, "100": 1, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0, '0,50': 0, '0,20': 0,
		'0,10': 0, '0,05': 0, '0,02': 0, '0,01': 0}

def dic_foat(dic: dict):
	summe = 0
	for key, val in dic.items():
		key = key.replace(',', '.')
		summe += float(key) * val
	return summe

def rueckgabe_summe(erhalten, kaufpreis):
	return erhalten - kaufpreis


def rueckgabe_einheiten(wechselgeld):
	geld = {"500": 0, '200': 0, "100": 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0, '0,50': 0, '0,20': 0,
			'0,10': 0, '0,05': 0, '0,02': 0, '0,01': 0}
	for key, val in geld.items():
		key_int = float(key.replace(',', '.'))
		while key_int < wechselgeld:
			geld[key] += 1
			wechselgeld -= key_int
	return geld
print(dic_foat(geld))
print(rueckgabe_einheiten(rueckgabe_summe(dic_foat(geld), kaufpreis)))
produkte = [
	{'id': 40158, 'name': 'Laptop', 'preis': 10.0, 'anzahl': 4, 'mwst': 19},
	{'id': 49032, 'name': 'Tablet', 'preis': 12.5, 'anzahl': 2, 'mwst': 19},
	{'id': 96590, 'name': 'Smartphone', 'preis': 15.0, 'anzahl': 4, 'mwst': 7},
	{'id': 18036, 'name': 'Kaffeemaschine', 'preis': 17.5, 'anzahl': 6, 'mwst': 19},
	{'id': 73245, 'name': 'Kühlschrank', 'preis': 20.0, 'anzahl': 8, 'mwst': 19},
	{'id': 51449, 'name': 'Waschmaschine', 'preis': 22.5, 'anzahl': 10, 'mwst': 7},
	{'id': 24910, 'name': 'Fernseher', 'preis': 25.0, 'anzahl': 12, 'mwst': 7},
	{'id': 12764, 'name': 'Kamera', 'preis': 27.5, 'anzahl': 14, 'mwst': 7},
	{'id': 17308, 'name': 'Monitor', 'preis': 30.0, 'anzahl': 16, 'mwst': 19},
	{'id': 74501, 'name': 'Headset', 'preis': 32.5, 'anzahl': 18, 'mwst': 7},
	{'id': 95951, 'name': 'Tastatur', 'preis': 35.0, 'anzahl': 20, 'mwst': 19},
	{'id': 47012, 'name': 'Maus', 'preis': 37.5, 'anzahl': 22, 'mwst': 19},
	{'id': 19274, 'name': 'Drucker', 'preis': 40.0, 'anzahl': 24, 'mwst': 19},
	{'id': 36044, 'name': 'Lautsprecher', 'preis': 42.5, 'anzahl': 26, 'mwst': 7},
	{'id': 67299, 'name': 'Mikrowelle', 'preis': 45.0, 'anzahl': 28, 'mwst': 19},
	{'id': 48291, 'name': 'Staubsauger', 'preis': 47.5, 'anzahl': 30, 'mwst': 7},
	{'id': 25900, 'name': 'Router', 'preis': 50.0, 'anzahl': 32, 'mwst': 7},
	{'id': 96962, 'name': 'Schreibtischlampe', 'preis': 52.5, 'anzahl': 34, 'mwst': 7},
	{'id': 94091, 'name': 'Smartwatch', 'preis': 55.0, 'anzahl': 36, 'mwst': 7},
	{'id': 34546, 'name': 'Gaming-Stuhl', 'preis': 57.5, 'anzahl': 38, 'mwst': 19}
]


def berechne_summe(produkte):
	summe = 0
	for produkt in produkte:
		summe += produkt['anzahl'] * produkt['preis']
	return summe


def mwst(mwst, produkte):
	mwst_betrag = 0

	for x in produkte:
		if mwst == x['mwst']:
			mwst_betrag += ((x['preis'] * 100 / (100 + mwst)) - x['preis'])


# print(berechne_summe(produkte))

print((6.48 * 100 / (100 + 19)) - 6.48)
