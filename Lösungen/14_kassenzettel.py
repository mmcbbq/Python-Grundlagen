import datetime

produkte = [
    {'id': 40158, 'name': 'Laptop', 'preis': 100.0, 'anzahl': 4, 'mwst': 19},
    {'id': 49032, 'name': 'Tablet', 'preis': 12.5, 'anzahl': 2, 'mwst': 19},
    {'id': 96590, 'name': 'Smartphone', 'preis': 15.0, 'anzahl': 4, 'mwst': 7},
    {'id': 18036, 'name': 'Kaffeemaschine', 'preis': 17.5, 'anzahl': 6, 'mwst': 19},
    {'id': 73245, 'name': 'Kühlschrank', 'preis': 20.0, 'anzahl': 8, 'mwst': 19},
    {'id': 51449, 'name': 'Waschmaschine', 'preis': 22.5, 'anzahl': 10, 'mwst': 7}
]

kunde_gibt = {"500": 2, '200': 0, "100": 1, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0, '0,50': 0, '0,20': 0,
              '0,10': 0, '0,05': 0, '0,02': 0, '0,01': 0}


#                  Kaufland
#              Berlinerstr. 120
#                Berlin 10000
#              Tel: 030/123456
#                                Preis Euro
# Laptop
#    4 * 100.00                     400.00
# Tablet
#    2 * 12.50                       25.00
# Smartphone
#    4 * 15.00                       60.00
# Kaffeemaschine
#    6 * 17.50                      105.00
# Kühlschrank
#    8 * 20.00                      160.00
# Waschmaschine
#   10 * 22.50                      225.00
# Summe                             975.00
# Euro                    €        1100.00
# Rückgeld                          125.00
# Steuer %   Brutto   Netto         Steuer
# A 19,00%   690.00 579.83          110.17
# B 07,00%   285.00 266.36           18.64
#
#   Datum: 31.10.24	 Zeit:  10:59:15

# ALLE floats auf 2 stellen runden
def produkt_kaufpreis(prod_dic: dict) -> float:
    return round(prod_dic['anzahl'] * prod_dic['preis'], 2)


def summe_kaufpreis(prod_list: list) -> float:
    summe = 0
    for prod_dic in prod_list:
        summe += produkt_kaufpreis(prod_dic)
    return round(summe, 2)


def brutto_mwst_19(prod_list: list) -> float:
    summe = 0
    for produkt in prod_list:
        if produkt['mwst'] == 19:
            summe += produkt['preis'] * produkt['anzahl']
    return round(summe, 2)


def brutto_mwst_7(prod_list: list) -> float:
    summe = 0
    for produkt in prod_list:
        if produkt['mwst'] == 7:
            summe += produkt['preis'] * produkt['anzahl']
    return round(summe, 2)


def netto_mwst_19(prod_list: list) -> float:
    brutto = brutto_mwst_19(prod_list)
    netto = brutto * 100 / (100 + 19)
    return round(netto, 2)


def netto_mwst_7(prod_list: list) -> float:
    brutto = brutto_mwst_7(prod_list)
    netto = brutto * 100 / (100 + 7)
    return round(netto, 2)


def mwst_betrag_19(prod_list: list) -> float:
    return round(brutto_mwst_19(prod_list) - netto_mwst_19(prod_list), 2)


def mwst_betrag_7(prod_list: list) -> float:
    return round(brutto_mwst_7(prod_list) - netto_mwst_7(prod_list), 2)


def kunden_zahlt(geld_dic: dict) -> float:
    summe = 0
    for key, val in geld_dic.items():
        summe += float(key.replace(',', '.')) * val
    return round(summe, 2)


def kunde_rueckgeld(kaufpreis: float, bezahlt: float) -> float:
    return round(bezahlt - kaufpreis, 2)


def print_kassenzettel(prod_liste: list, geld_dic: dict) -> str:
    kasse = ''
    kasse += f"{'Kaufland':^50}\n"
    kasse += f"{'Berlinerstr. 120':^50}\n"
    kasse += f"{'Berlin 10000':^50}\n"
    kasse += f"{'Tel: 030/123456':^50}\n"
    kasse += f'{"Preis Euro":>45}\n'
    for x in prod_liste:
        kasse += f'\t{x["name"]}\n'
        kasse += f'\t{x["anzahl"]:>4} * {x["preis"]:<7.2f} {produkt_kaufpreis(x):>25.2f}\n'
    kasse += f'\t{"Summe"}{summe_kaufpreis(prod_liste):>35.2f}\n'
    kasse += f'\t{"Euro"} {"€":>20}{kunden_zahlt(geld_dic):>15.2f}\n'
    kasse += f'\t{"Rückgeld"}{kunde_rueckgeld(summe_kaufpreis(prod_liste), kunden_zahlt(geld_dic)):>32.2f}\n'
    kasse += f'\t{"Steuer %"}  {"Brutto":>7} {"Netto":>7} {"Steuer":>14}\n'
    kasse += f'\tA 19,00% {brutto_mwst_19(prod_liste):>8.2f} {netto_mwst_19(prod_liste):.2f} {mwst_betrag_19(prod_liste):>15.2f}\n'
    kasse += f'\tB 07,00% {brutto_mwst_7(prod_liste):>8.2f} {netto_mwst_7(prod_liste):.2f} {mwst_betrag_7(prod_liste):>15.2f}\n'
    x = datetime.datetime.now()
    datum_string = f'Datum: {x.strftime("%d.%m.%y")}\t Zeit:  {x.strftime("%H:%M:%S")}\n'
    kasse += '\n'
    kasse += f'{datum_string:^50}\n'
    return kasse
    pass


def wechsel_geld(rueckgeld: float) -> dict:
    # Liste der verfügbaren Scheine und Münzen (von groß zu klein)
    geld = {"500": 0, '200': 0, "100": 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0, '0,50': 0, '0,20': 0,
            '0,10': 0, '0,05': 0, '0,02': 0, '0,01': 0}
    for key, val in geld.items():
        key_float = float(key.replace(',', '.'))
        while rueckgeld >= key_float:
            geld[key] += 1
            rueckgeld -= key_float
            rueckgeld = round(float(rueckgeld), 2)
    return geld


def print_def_wechsel(ruck: float) -> None:
    for x, y in wechsel_geld(ruck).items():
        if y == 0:
            continue
        print(f'{x}: {y}')


print(print_kassenzettel(produkte, kunde_gibt))
print_def_wechsel(kunde_rueckgeld(summe_kaufpreis(produkte), kunden_zahlt(kunde_gibt)))