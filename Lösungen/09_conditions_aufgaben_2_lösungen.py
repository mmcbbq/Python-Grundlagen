# Der Benutzer soll zwei Zahlen in das Programm eingeben, danach soll er entscheiden, ob die Zahlen addiert,
# subtrahiert, multipliziert oder dividiert werden, diese Entscheidung soll über die Eingabe der folgenden
# Symbole getätigt werden: +, -, *, /
# Bei der Division durch 0 soll die Ausgabe "Das kann nur Chuck Norris" erfolgen
# Nach der Auswahl soll das Ergebnis der Rechnung ausgegeben werden,
# bzw. eine Fehlermeldung, falls eine
# falsche Auswahl getroffen wurde.
zahl1 = int(input("Zahl 1"))
operator = input("Rechenart +, -, *, /")
zahl2 = int(input("Zahl 2"))
# #
if operator == "+":
	solution = zahl1 + zahl2

elif operator == "-":
	solution = zahl1 - zahl2

elif operator == "*":
	solution = zahl1 * zahl2

elif operator == "/":
	if zahl2 == 0:
		solution = "Das kann nur Chuck Norris"
	else:
		solution = zahl1 / zahl2
print(solution)
# exec("print(5 + 3)")


# Nach dem Ohmschen Gesetz berechnet sich der Widerstand eines ohmschen Widerstandes mit:
# U = R * I
# R = U/I
# I = U/R
# Schreiben Sie ein Programm, in das der Benutzer zunächst über die Eingabe der Buchstaben R, U oder I
# auswählen kann, welche Größe berechnet werden soll. Gibt er einen falschen Buchstaben ein, soll eine Meldung
# über die Fehleingabe erfolgen.
# Anschließend soll er die Werte der fehlenden Größen eingeben. Am Ende gibt das Programm den Wert der
# gesuchten Größe mit der richtigen Einheit aus
uri = input(' U R I')
uri = uri.upper()
if uri == 'U':
	r = float(input('R wert'))
	i = float(input('I wert'))
	print('U=:', r * i, 'Volt')
elif uri == 'R':
	u = float(input('U wert'))
	i = float(input('I wert'))
	print('R=:', u / i, 'Ohm')
elif uri == 'I':
	r = float(input('R wert'))
	u = float(input('U wert'))
	print('I=:', u / r, 'Ampere')
else:
	print('Falsche Eingabe')

# Ein Hardware-Großhändler führt ein Rabattsystem für Stammkunden ein: Liegt der Bestellwert zwischen 0 und
# 100 €, erhält der Kunde einen Rabatt von 10 %. Liegt der Bestellwert höher, aber insgesamt nicht über 500 €,
# beträgt der Rabatt 15 %, in allen anderen Fällen beträgt der Rabatt 20 %. Nach Eingabe des Bestellwertes soll
# der ermäßigte Bestellwert berechnet und ausgegeben werden.

bestellwert = float(input('Bestellwert?'))
if 0 < bestellwert <= 100:
	print(bestellwert * 0.9)
elif 100 < bestellwert < 500:
	print(bestellwert * 0.85)
elif bestellwert >= 500:
	print(bestellwert * 0.8)
else:
	print('Falsche Eingabe')

# Der BMI berechnet sich aus dem Körpergewicht [kg] dividiert durch das Quadrat der Körpergröße [m2
# Die Formel lautet: BMI = (Körpergewicht in kg)\ (Körpergröße in m)**2
# Der BMI einer Person wird nach den
# folgenden Regeln klassifiziert (nach DGE, Ernährungsbericht 1992):
# Klassifikation m w
# Untergewicht < 20 < 19
# Normalgewicht 20-25 19-24
# Übergewicht 25-30 24-30
# Adipositas 30-40 30-40
# massive Adipositas > 40 > 40
# Das Programm soll vom Benutzer das Gewicht [in kg] die Größe [in cm] und das Geschlecht [m/w] abfragen. Am
# Ende des Programms soll die BMI-Klassifikation der Person ausgegeben werden.
#
gewicht = float(input('Gewicht in kg'))
grosse = float(input('Größe in cm'))
geschlecht = input('Geschlecht m w')
bmi = gewicht / (grosse / 100) ** 2




if 30 <= bmi < 40:
	print('Adipositas')
elif bmi >= 40:
	print('massive Adipositas')
elif geschlecht == "w":
	if bmi < 19:
		print('Untergewicht')
	elif 19 <= bmi < 24:
		print('Normalgewicht')
	elif 24 <= bmi < 30:
		print('Übergewicht')
elif geschlecht == "m":
	if bmi < 20:
		print('Untergewicht')
	elif 20 <= bmi < 25:
		print('Normalgewicht')
	elif 25 <= bmi < 30:
		print('Übergewicht')









if bmi >= 40:
	print("massive Adipositas")
elif bmi >= 30 and bmi < 40:
	print('Adipositas')
elif geschlecht == "w" and bmi < 30 and bmi >= 24 or geschlecht == "m" and bmi < 30 and bmi >= 25:
	print('Übergewicht')
elif geschlecht == "w" and bmi < 24 and bmi >= 19 or geschlecht == "m" and bmi < 25 and bmi >= 20:
	print('Normalgewicht')
elif geschlecht == "w" and bmi < 19 or geschlecht == "m" and bmi < 20:
	print('Untergewicht')


# Schaltjahres-Berechnung
# Eingabe eines Jahres -> Ausgabe Schaltjahr, kein Schaltjahr
# Laut Kalender hat ein Jahr 365 Tage. Die Erde braucht aber 365 Tage, 5 Stunden, 48 Minuten und 45 Sekunden, um die Sonne zu umrunden. Der Schalttag gleicht diese Differenz aus – allerdings nicht ganz, dazu sind die Zahlen zu unrund. Denn die überzähligen Stunden, Minuten und Sekunden addieren sich nach vier Jahren zu etwa 23 Stunden und 11 Minuten – also keinem ganzen Tag.
# Im Jahr 1582 veranlasste Papst Gregor eine Kalenderreform. Seitdem gilt der Gregorianische Kalender mit den folgenden Regeln zur Schaltjahresberechnung:
#
#
#
# Bedingung 1:
# Ist eine Jahreszahl ganzzahlig durch 4 teilbar, dann ist das Jahr ein Schaltjahr.
# Testwerte: 1720, 1972 und 1980 waren Schaltjahre.
# Bedingung 2:
# Ausnahme zu den Jahreszahlen, die der Bedingung 1 genügen, sind alle Jahreszahlen,
# die nach Bedingung 1 ein Schaltjahr sind, aber deren Jahreszahl ganzzahlig durch 100 teilbar ist.
# Testwerte: 1700, 1800 und 1900 oder ferner 2100 sind keine Schaltjahre.
# Bedingung 3:
# Ausnahme zu den Jahreszahlen, die der Bedingung 2 genügen, sind alle Jahreszahlen,
# die nach Bedingung 2 kein Schaltjahr sind, aber deren Jahreszahl ganzzahlig durch 400 teilbar.
# Testwerte: 1600 und 2000 waren Schaltjahre.
jahr = int(input('Jahr'))

if jahr % 4 != 0:
	print('kein Schaltjar')
elif jahr % 100 == 0:
	if jahr % 400 == 0:
		print('Schaltjahr')
	else:
		print('kein Schaltjahr')
else:
	print('Schaltjahr')
jahr = int(input("Bitte gebe das Jahr an\n"))
if jahr % 4 == 0:
	if jahr % 100 == 0:
		if jahr % 400 == 0:
			print("Schaltjahr")
		else:
			print("keine Schaltjahr")
	else:
		print("Schaltjahr")
else:
	print("kein Schaltjahr")

years = [1720, 1972, 1980, 1700, 1800, 2100, 1600, 2000, 1200]
for year in years:


	if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
		print('kein Schaltjahr')
	else:
		print(' Schaltjahr')

	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		print(' Schaltjahr  ++')
	else:
		print('kein Schaltjahr ++')



# Aufgabe: Berechnung der Energieverbrauchskosten
# Erstelle ein Programm, das die monatlichen Energiekosten eines Haushalts basierend auf dem Energieverbrauch berechnet. Dabei werden unterschiedliche Preise für verschiedene Verbrauchsstufen und ein Bonus für energiesparende Haushalte berücksichtigt.
#
# Berechnung:
# Basispreis:
#
# Für die ersten 100 kWh: 0,30 Euro pro kWh
# Für die nächsten 200 kWh (zwischen 101 kWh und 300 kWh): 0,25 Euro pro kWh
# Für den Verbrauch über 300 kWh: 0,20 Euro pro kWh
# Bonus für energiesparende Haushalte:
#
# Wenn der gesamte Verbrauch unter 150 kWh liegt, erhält der Haushalt einen Bonus von 10 Euro, der von den Gesamtkosten abgezogen wird.
# Das Programm sollte den Benutzer nach dem monatlichen Energieverbrauch in kWh fragen und dann die Gesamtkosten unter Berücksichtigung der oben genannten Bedingungen berechnen.

test = [149, 150, 151, 299, 300, 301, 199, 99, 100, 101]

verbraucht = int(input('Verbrauch:\n'))
if verbraucht < 0:
	preis = 0
elif verbraucht < 150:
	if verbraucht <= 100:
		preis = verbraucht * 0.3 - 10
	else:
		preis = (verbraucht - 100) * 0.25 + 100 * 0.3 - 10
elif verbraucht >= 150:
	if verbraucht > 300:
		preis = (verbraucht - 300) * 0.2 + 200 * 0.25 + 100 * 0.3
	else:
		preis = (verbraucht - 100) * 0.25 + 100 * 0.3
if preis < 0:
	preis = 0
print(f"preis: {preis} Euro ")

preis = 0
















