# Die input()-Funktion in Python wird verwendet,
# um Benutzereingaben über die Konsole zu erhalten.
# Sie erlaubt es dem Benutzer, Daten während der Programmausführung einzugeben.

name = input('Wie ist dein Name')
print('Hallo', name)

# Die input()-Funktion nimmt einen String als Argument, die dem Benutzer angezeigt wird, um ihn zur Eingabe
# aufzufordern. "Wie ist dein Name"
# Die eingegebene Zeichenkette wird als Rückgabewert der input()-Funktion verwendet
# und kann einer Variablen zugewiesen werden (name in diesem Fall).


antwort = input('Schreib deinen namen:\n')

# Standardmäßig gibt input() die vom Benutzer eingegebene Zeichenkette zurück,
# auch wenn der Benutzer eine Zahl eingibt.
# Wenn du eine Zahl benötigst, musst du die Rückgabe von input() in einen numerischen Typ umwandeln:

alter = int(input('Schreib dein Alter'))
print(antwort, type(antwort))
print(alter, type(alter))
