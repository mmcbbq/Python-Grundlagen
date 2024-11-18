import datetime

produkte = [
	{'id': 40158, 'name': 'Laptop', 'preis': 10.0, 'anzahl': 10000, 'mwst': 19},
	{'id': 49032, 'name': 'Tablet', 'preis': 11112.5, 'anzahl': 2, 'mwst': 19},
	{'id': 96590, 'name': 'Smartphone', 'preis': 15.0, 'anzahl': 114, 'mwst': 7},
	{'id': 18036, 'name': 'Kaffeemaschine', 'preis': 17.5, 'anzahl': 6, 'mwst': 19},
	{'id': 73245, 'name': 'Kuhlschrank', 'preis': 20.0, 'anzahl': 8, 'mwst': 19},
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
date = datetime.datetime.now()
print(date.strftime("%B %m"))
for prod in produkte:
    summe = prod['anzahl'] * prod['preis']
    print(f'{prod["name"]} ')
    # print(f'{prod["anzahl"]} * {prod["preis"]:.2f}{"":<50}{str(summe).rjust(10)}')
    print(f'{prod["anzahl"]:>4} * {prod["preis"]:>10.2f}{summe:>20.2f}')