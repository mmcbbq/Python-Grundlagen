
# Eine Variable im allgemeinsten Sinne ist einfach ein Behälter (Container) zur Aufbewahrung von bestimmten Werten.
# Eine Variable wird definiert, indem ich einen Namen vergebe und mit dem zuweisungsoperator = diese "Behälter" völle.
my_var = "Hallo Welt"
# Ein Variablenname muss mit einem Buchstaben anfangen. Es ist allgemeine praxis kleine Buchstaben zu verwenden.
# 666var = 666 geht nicht
# Var = "test" geht aber soll man nicht machen

# Variablennamen dürfen Zahlen und _ sowie Umlaute enthalten. Umlaute sollte man vermeiden
my_var2üöa = ""

# Folgende Wörter sind nicht erlaubt da sie von Python verwendet werden.
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# Es sollten auch keine Eingebauten Funktionsnamen benutzt werden da diese sonst überschrieben werden.

# print = 212 geht aber soll man nicht machen

# in Pep 8 wird der Snakecase benutzt
test = 1
testNummer = 100  # kann man machen
test_nummer = "test"  # sollte man machen
print(test)

# Vor dem Aufrufen müssen Variablen definiert werden
#print(aufruf) # erzeugt einen error
aufruf = "falsch"
# Man kann beliebig viele Variablen erstellen
name1 = "Bob"
name2 = "Jones"
name3 = "Jim"
print(name1)

# Variablen kann man überschreiben
name = "Tim"
name = "Bob"
print(name1)

# Bei der Zuweisung von Variablen kann ich mathematische Operationen durchführen
# ebenso können bei der Zuweisung Variablen verwendet werden
zahl = 300 + 100
wort = "Test" * zahl
print(zahl)
print(wort)


# Um eine Variable hochzuzählen wird die Variable bei der Zuweisung selbst Aufgerufen
bob_autos = 1
bob_autos = bob_autos + 1

bob_autos += 1 # Das ist die kurz Schreibweise für Zeile 49

# Man kann alle anderen mathematische Operationen verwenden
bob_autos -= 1
bob_autos *= 5
bob_autos /= 3
bob_autos -= 500
print(bob_autos)

# In anderen Sprachen kann man auch ++bob_autos --bob_autos verwenden


# In Python kann man viele Variablen in einer Zeile definieren
a, b, c = 5, 3, 2
print(a,b)

# Um Variablenwerte zu tauschen, benötigt man einen Zwischenspeicher
zwisch = a
a = b
b = zwisch
print(a,b)
# In Python kann man dies aber auch wie folgt lösen
a, b = b, a
print(a, b)

