# Ein string ist eine Sequenz von Zeichen
# Strings werden mit ' oder " umschlossen
my_string = "Hello"
my_string2 = 'Hello'
# Einen mehr Zeiliger String kann man mit ''' oder """ erstellen

long_string = """Hallo
ich
				bin 
ein 
langer 
string"""
print(long_string)
long_string2 = '''Hallo
ich
bin 
ein 
langer 
string'''
print(long_string2)

# String kann ich mit anderen Strings mit + verbinden
print("hallo" + "Welt")
string1 = "test"
string2 = "super"
print(string1 + ' ' + string2)

# print(string1+5) geht nicht


# Strings kann mit Zahlen auch multiplizieren
print(8 * string1 * 5)
# print(string1 * string2) geht nicht


# String Slicing -> den String zurechtschneiden

a = "Python ist super toll"
# Möchte ich nur das Wort Python
b = a[0:6]  # die Variable ansprechen und in [] definieren welche Stellen man ausschneiden möchte
# von der 0 Stelle ist das erste Zeichen. Da Computer immer bei = anfagen zu zählen
# bis zur 6 Stelle aber nicht inklusiv der 6 Stelle
print(b)

# von der 12 bis zur 15 -> super
c = a[11:16]
print(c)

# wenn man die erste Stelle frei lässt startet er am anfang
d = a[:6]
print(d)
# wenn man die letzte Stelle frei lässt mach er bis zum Ende

e = a[7:]
print(e)

# negative index zählt von hinten
# die letzte Stelle ist -1
# und er zählt bis zur -5 stelle aber nicht inklusive
f = a[-10:-5]
print(f)

# um einzehlnde Buchstaben gibt man nur diese Stelle an ohne eine weiteren Wert mit : zu definieren
print(a[0], a[7], a[-10], a[-4]),
f = a[7:10] + a[-5:]
print(f)

# Die String Methode lower ersetzt alle Großbuchstaben gegen Kleinbuchstaben
name = "Peter Pan"
name_klein = name.lower()
print(name_klein)
# gegenteil von lower
name_groß = name.upper()
print(name_groß)
# Die replace Methode taucht eine Zeichen gegen einen Anderen aus
# Die replace Methode benötigt 2 Argumente
# Das erste Argument ist das zu ersetzende Zeichen
# Das zweite Argument ist das Zeichen mit dem das erste Getauscht werden soll
username = name.replace(" ", "_")
print(username.lower())

# Einen String in einem Linuxusernamen ändern
name2 = "Peter Pan"
name_am_anfang_gross = name2[0].upper() + name2[1:]
print(name_am_anfang_gross)

# Die len Funktion gibt die Anzahl der Zeichen wieder
print("länge", len(name2))
