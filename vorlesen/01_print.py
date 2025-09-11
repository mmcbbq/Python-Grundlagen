# Die print Funktion ist eine in Python eingebaute Funktion.
# Eine Liste von allen eingebauten Funktionen. https://docs.python.org/3/library/functions.html#func-list

# Um eine Funktion zu benutzen, muss man sie aufrufen oder function call oder function invocation
# Man schreibt den funktionsnamen gefolgt von Klammer auf klammer zu "()"
print()
# Zwischen den Klammern kann man nun Argumente übergeben.

print('Hello World!')

# Bei vielen Funktionen kann man auch mehrere Argumente übergeben.
# Diese müssen mit einem Komma getrennt werden.
print("Hallo", "Welt ", "Wie geht es dir")
# Es gibt 2 arten Positinal und Keyword arguments

# Bei Positianl arguments ist die Reihenfolge wichtig.
# Keyword arguments bei diesen ist die Position egal.
# Sie werden mit einem für die Funktion speziellen Keyword angesprochen.
# Für print die end und sep Keyword arguments

# Die print Funktion sendet Informationen an die Konsole

# Die print Funktion übergibt man ein string
print("Hallo Welt")
# Um in den String eine newline zu erzeugen kann man \n dies tun.
print("Hallo \nWelt")
#
# Das Zeichen \ wird auch benutzt um Sonderzeichen wie \" darzustellen.

print("Hallo mein Name ist \"Manuel\" mein Homeorderner ist \\home\\manuel")

# mit \t macht man ein Tabulator
print("Das", "\tist", "\tein", "\ttab")

# Das Keyword argument sep definiert die Zeichen zwischen 2 positional argumetns
# Default ist sep=" "
print("Das", "ist")
print("Das", "ist", sep="+++")
print("Hallo mein Name", "ist", "Bob", sep="***", end='+++')

# Das Keyword argument end definiert die Zeichen am Ende der print Funktion
# Default ist end="\n".
print("Hallo")
print("Welt")

print("Hallo", end="Ende der Zeile")
print("Welt", end="Ende der Zeile")
