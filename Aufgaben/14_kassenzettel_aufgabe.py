# Gegeben ist eine Liste mit Dictionary von Produkten die gekauft werden sollen.

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
    # TODO: Berechne den Kaufpreis als (Anzahl x Preis) und gib ihn zurück. Zeile 22 400.00
    pass


def summe_kaufpreis(prod_list: list) -> float:
    # TODO: Berechne den Kaufpreis aller Produkte in der Liste mit hilfe der produkt_kaufpreis func Zeile 33 975.00
    pass


def brutto_mwst_19(prod_list: list) -> float:
    # TODO: Berechne den Bruttopreis aller Produkte mit 19% Zeile 37: 690.00
    pass


def brutto_mwst_7(prod_list: list) -> float:
    # TODO: Berechne den Bruttopreis aller Produkte mit 7% Zeile 38: 285.00
    pass


def netto_mwst_19(prod_list: list) -> float:
    # TODO: Berechne den Nettopreis aller Produkte mit 19% Zeile 37: 579.83
    pass


def netto_mwst_7(prod_list: list) -> float:
    # TODO: Berechne den Nettopreis aller Produkte mit 7% Zeile 38: 266.36
    pass


def mwst_betrag_19(prod_list: list) -> float:
    # TODO: Berechne die Mwst_betrag aller Produkte mit 19% Zeile: 37 110.17
    pass


def mwst_betrag_7(prod_list: list) -> float:
    # TODO: Berechne die Mwst_betrag aller Produkte mit 7% Zeile 38: 18.64
    pass


def kunden_zahlt(geld_dic: dict) -> float:
    # TODO: Berechen die vom Kunden erhalten Geldsumme Zeile:34 1100.00
    pass


def kunde_rueckgeld(kaufpreis: float, bezahlt: float) -> float:
    # TODO: Berechen das Rückgeld Zeile:35 125.00
    pass


def print_kassenzettel(prod_liste: list, geld_dic: dict) -> str:
    # TODO: Erstelle einen string siehe oben
    pass


def wechsel_geld(rueckgeld: float) -> dict:
    # Liste der verfügbaren Scheine und Münzen (von groß zu klein)
    geld = {"500": 0, '200': 0, "100": 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0, '0,50': 0, '0,20': 0,
            '0,10': 0, '0,05': 0, '0,02': 0, '0,01': 0}
    # TODO:  Definiere eine Funktion, die berechnet, wie viele Scheine und Münzen ein Kassierer zurückgeben muss.
    pass
