# Funktionen sind wiederverwendbare Codeblöcke,
# die eine bestimmte Aufgabe erledigen.


# Vorteile von Funktionen beim Programmieren
#
# Lesbarkeit und Wartbarkeit:
# Funktionen sind oft leichter zu lesen und zu verstehen als einzelne Codeblöcke.
# Dies liegt daran, dass sie eine einzelne Aufgabe erledigen
# und klare Grenzen haben. Funktionen sind auch leichter zu warten,
# da Änderungen an einer Funktion nur Auswirkungen auf den Code haben,
# der sie aufruft.
#
# Verifikation und Testbarkeit:
#
# Funktionen sind leichter zu verifizieren und zu testen als einzelne Codeblöcke.
# Dies liegt daran, dass sie eine einzelne Aufgabe erledigen
# und klare Grenzen haben. Funktionen können einzeln getestet werden,
# ohne dass der Rest des Codes berücksichtigt werden muss.
#
# Modularität und Abstraktion
#
# Funktionen ermöglichen es, Code zu modularisieren und zu abstrahieren.
# Dies macht den Code leichter zu verstehen und zu verwalten.
# Funktionen können auch verwendet werden, um komplexe Aufgaben in kleinere,
# einfachere Aufgaben zu zerlegen.
#
# Rekursion und elegante Lösungen
#
# Funktionen ermöglichen es, Rekursion zu verwenden.
# Rekursion ist eine Technik, bei der eine Funktion sich selbst aufruft,
# um eine Aufgabe zu erledigen.
# Rekursion kann verwendet werden,
# um komplexe Aufgaben auf elegante Weise zu lösen.
#

# In Python eingebaute Funktionen
# print()
# input()
# range()
# len()
# str()
# int()
# float()
# sum()
# max()
# min()

# Um eine Funktion zu definieren, fängt man mit dem "def" Keyword an
# In anderen Programmiersprachen function oder int
# gefolgt von einem aussagekräftigen Funktionsnamen
# und abschliessen ()
def sag_hallo():
    print('Hallo')  # Der Funktionskörper wird mit einrückungen definiert. Er wird erst beim Aufruf ausgeführt.


sag_hallo()  # Der Funktionsaufruf erfolgt über den Namen der Funktion mit ()


# Funktionen müssen vor dem Aufruf definiert werden.
# my_func() -> NameError: name 'my_func' is not defined
#
# def my_func():
# 	print('my_func')


# Bei der Definition können optional Parameter zwischen den Klammeren übergeben werden.
# Parameter sind Platzhalter oder Variablen,
# die in der Funktionsdefinition verwendet werden,
# um Werte zu akzeptieren, die der Funktion übergeben werden sollen.
def sag_hallo_mit_namen(name):
    print('Hallo ', name)


# Bei dem Funktionsaufruf müssen die Parameter mit tatsächlichen Werten gefühlt werden.
# Diese Werte nennt man Argumente

sag_hallo_mit_namen('Bob')  # Das Argument 'Bob' wird bei dem Funktionsaufruf dem Parameter name zugewiesen.


# Beim Aufruf der Funktion stop das Programm und springt in die Funktion.
# name = 'Bob'
# print('Bob')
# Wenn die Funktion ein Argument benötigt aber keines Übergeben wird, erhält man einen Fehler
# sag_hallo_mit_namen() -> sag_hallo_mit_namen() missing 1 required positional argument: 'name'

# man kann Beliebig viele Parameter festlegen
def my_sum(a: str, b: int) -> None:
    """super summer"""
    print(a * b)


# Bei dem Aufruf der Funktion werden die Argumente in der reihenfolge nach übergeben
# a = 8 b = 9
my_sum(8, 9)


# Funktionen können Rückgabewerte enthalten. return value.
def my_sum_return(a, b):
    summe = a + b
    return summe


# Diese return values werden bei dem Ausführen des Programmes an die Stelle gesetzt an dem die Funktion aufgerufen wird

var_my = my_sum_return(my_sum_return(1,2), 10)  # ->18
# var_my = 18
print(var_my)


def my_string():
    return 'Hallo'


# Return values haben dieselben eigenschaften wie die Datentypen die sie repräsentieren

print(my_string())
print(len(my_string()))

print(my_string()[0:3])


def print_liste(liste):
    for x in liste:
        print(x)


my_liste = ['Hallo', 1, True, 'Bob', 12.456]

print_liste(my_liste)


# Funktionen akzeptieren nicht nur Feste Werte sonder auch Variablen oder andere Funktionen als Argumente
def bigger(zahl1, zahl2):
    if zahl1 > zahl2:
        return zahl1
    elif zahl1 < zahl2:
        return zahl2
    else:
        return print('sind gleich')


z1 = 5
z2 = 3
print(bigger(z1, z2))


def mal_5(a):
    return a * 5


print(bigger(mal_5(z1), z2))


# Wenn eine Funktion keine return value definiert gibt sie None zurück
# None ist ein eigener Datentyp in Python

def no_return():
    test = 5 * 20


print(no_return())  # -> None


def check_list(liste):
    for x in liste:
        if x == 1:
            return f'{x} ist da'
        print(x)


my_liste = [5, 8, 1, 2, 6, 8, 1]
# Sobald eine Funktion auf eine return triff stop diese Funktion und gibt den return value wieder.
# Es kann nur einen return value geben
print(check_list(my_liste))


# Man kann beliebig viele Parameter festlegen

def sag_name(vorname, nachname):
    print(vorname, nachname)


sag_name('Bob', 'Bobson')
sag_name('Bobson', 'Bob')


def div(x, y=2):  # Wir ein default value für y definiert
    return x / y


print(div(10))  # Bei dem Aufruf der Funktion muss dieser nicht als Argument übergeben werden x = 10 y = 2

print(div(15, 3))  # Er kann aber überschrieben werden x = 15 y = 3
print(div(3, 15))  # Die positonen der Argumente ist wichtig

# Die definierten Parameter kann man auch als Keyword arguments übergeben
print('###############Keyword############################')
print(div(x=15, y=3))
print(div(y=3, x=15))


# In Python muss man die Positional arguments definieren vor den Keyword arguments
# print(div(x=20 , 23)) -> positional argument follows keyword argument

def my_func_pkd(x, y, z=100):
    return x + y + z


print(my_func_pkd(100, z=120, y=50))


# New feature since Python 3.8
# positional arguments before /: a und b
# optional arguments zwischen / * c und d
# keyword arguments nur nach dem * e

def boo(a, b, /, c, d, *, e=100):
    print(f"a:{a}")
    print(f"b:{b}")
    print(f"c:{c}")
    print(f"e:{e}")


boo(1, 2, c=3, d=5)

boo(1, 2, 3, 4, e=10)


# boo(1,2,3,4, 5) -> boo() takes 4 positional arguments but 5 were given


# Wenn man eine vorher unbestimmte Zahl von Parametern uebergeben will, kann man dies mit *param
# Diese Parameter werden in ein tuple gepackt
def keineplan(*viele_oder_eins, key) -> str:
    print(type(viele_oder_eins))
    print(viele_oder_eins)
    print(key)
    return "test"


keineplan(1, 2, 3, 4, "test", 9, key=12)
