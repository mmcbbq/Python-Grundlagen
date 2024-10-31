import datetime


def berechne_geld(dic):
	summe = 0
	for key, val in dic.items():
		summe += float(key.replace(',', '.')) * val
	return summe


def rueckgabe(kaufpreis, bezahlt):
	kaufpreis = int(kaufpreis * 100)
	bezahlt = int(bezahlt * 100)
	ruck = (bezahlt - kaufpreis) / 100
	return ruck


def wechsel_geld(betrag):
	# Liste der verfügbaren Scheine und Münzen (von groß zu klein)

	geld = {"500": 0, '200': 0, "100": 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0, '0,50': 0, '0,20': 0,
			'0,10': 0, '0,05': 0, '0,02': 0, '0,01': 0}
	for key, val in geld.items():
		key_float = float(key.replace(',', '.'))
		while betrag >= key_float:
			geld[key] += 1
			betrag -= key_float
			betrag = round(float(betrag), 2)
	return geld


def berechne_summe(prod_list):
	summe = 0
	for produkt in prod_list:
		summe += produkt['preis'] * produkt['anzahl']
	return summe


def berechen_summe_mwst(prod_list, mwst=19):
	summe = 0
	for produkt in prod_list:
		if produkt['mwst'] == mwst:
			summe += produkt['preis'] * produkt['anzahl']
	return summe


def mwst_netto(prod_list, mwst=19):
	brutto = berechen_summe_mwst(prod_list, mwst)
	netto = brutto * 100 / (100 + mwst)
	return netto


def steuer_betrag(brutto, netto):
	return brutto - netto


def print_kassen(produkt_list, geld):
	print(f"{'Kaufland':^50}")
	print(f"{'Berlinerstr. 120':^50}")
	print(f"{'Berlin 10000':^50}")
	print(f"{'Tel: 030/123456':^50}")
	print(f'{"Preis Euro":>45}')
	for x in produkt_list:
		print(f'\t{x["name"]}')
		print(f'\t{x["anzahl"]:>4} * {x["preis"]:<7.2f} {x["anzahl"] * x["preis"]:>25.2f}')
	print(f'\t{"Summe"}{berechne_summe(produkt_list):>35.2f}')
	print(f'\t{"Euro"} {"€":>20}{berechne_geld(geld):>15.2f}')
	print(f'\t{"Rückgeld"}{rueckgabe(berechne_summe(produkt_list), berechne_geld(geld)):>32.2f}')
	print(f'\t{"Steuer %"}  {"Brutto":>7} {"Netto":>7} {"Steuer":>14}')
	print(
		f'\tA 19,00% {berechen_summe_mwst(produkt_list):>8.2f} {mwst_netto(produkt_list):.2f} {steuer_betrag(berechen_summe_mwst(produkt_list), mwst_netto(produkt_list)):>15.2f}')
	print(
		f'\tB 07,00% {berechen_summe_mwst(produkt_list, 7):>8.2f} {mwst_netto(produkt_list, 7):.2f} {steuer_betrag(berechen_summe_mwst(produkt_list, 7), mwst_netto(produkt_list, 7)):>15.2f}')
	x = datetime.datetime.now()
	datum_string = f'Datum: {x.strftime("%d.%m.%y")}\t Zeit:  {x.strftime("%H:%M:%S")}'
	print()
	print(f'{datum_string:^45}')


def print_kassen_txt(produkt_list, geld_dic):
	kasse = ''
	kasse += f"{'Kaufland':^50}\n"
	kasse += f"{'Berlinerstr. 120':^50}\n"
	kasse += f"{'Berlin 10000':^50}\n"
	kasse += f"{'Tel: 030/123456':^50}\n"
	kasse += f'{"Preis Euro":>45}\n'
	for x in produkt_list:
		kasse += f'\t{x["name"]}\n'
		kasse += f'\t{x["anzahl"]:>4} * {x["preis"]:<7.2f} {x["anzahl"] * x["preis"]:>25.2f}\n'
	kasse += f'\t{"Summe"}{berechne_summe(produkt_list):>35.2f}\n'
	kasse += f'\t{"Euro"} {"€":>20}{berechne_geld(geld_dic):>15.2f}\n'
	kasse += f'\t{"Rückgeld"}{rueckgabe(berechne_summe(produkt_list), berechne_geld(geld_dic)):>32.2f}\n'
	kasse += f'\t{"Steuer %"}  {"Brutto":>7} {"Netto":>7} {"Steuer":>14}\n'
	kasse += f'\tA 19,00% {berechen_summe_mwst(produkt_list):>8.2f} {mwst_netto(produkt_list):.2f} {steuer_betrag(berechen_summe_mwst(produkt_list), mwst_netto(produkt_list)):>15.2f}\n'
	kasse += f'\tB 07,00% {berechen_summe_mwst(produkt_list, 7):>8.2f} {mwst_netto(produkt_list, 7):.2f} {steuer_betrag(berechen_summe_mwst(produkt_list, 7), mwst_netto(produkt_list, 7)):>15.2f}\n'
	x = datetime.datetime.now()
	datum_string = f'Datum: {x.strftime("%d.%m.%y")}\t Zeit:  {x.strftime("%H:%M:%S")}\n'
	kasse += '\n'
	kasse += f'{datum_string:^50}\n'
	return kasse


geld = {"500": 1, '200': 0, "100": 1, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0, '0,50': 0, '0,20': 0,
		'0,10': 0, '0,05': 0, '0,02': 0, '0,01': 0}


