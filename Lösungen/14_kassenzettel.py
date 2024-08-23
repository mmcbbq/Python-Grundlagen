import kassen_func

if __name__ == "__main__":
	geld = {"500": 2, '200': 0, "100": 1, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0, '0,50': 0, '0,20': 0,
			'0,10': 0, '0,05': 0, '0,02': 0, '0,01': 0}

	produkte = [
		{'id': 40158, 'name': 'Laptop', 'preis': 100.0, 'anzahl': 4, 'mwst': 19},
		{'id': 49032, 'name': 'Tablet', 'preis': 12.5, 'anzahl': 2, 'mwst': 19},
		{'id': 96590, 'name': 'Smartphone', 'preis': 15.0, 'anzahl': 4, 'mwst': 7},
		{'id': 18036, 'name': 'Kaffeemaschine', 'preis': 17.5, 'anzahl': 6, 'mwst': 19},
		{'id': 73245, 'name': 'Kühlschrank', 'preis': 20.0, 'anzahl': 8, 'mwst': 19},
		{'id': 51449, 'name': 'Waschmaschine', 'preis': 22.5, 'anzahl': 10, 'mwst': 7}
	]
	print(kassen_func.berechne_geld(geld))
	# kasse.print_kassen(produkte, geld)

	# f = open("kassenzettel.txt", "w")
	# f.write(print_kassen_txt(produkte, geld))
	# f.close()
