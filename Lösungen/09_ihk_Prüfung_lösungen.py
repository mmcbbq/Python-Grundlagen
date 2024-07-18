# Erstelle ein Programm, das überprüft,
# ob und mit welcher Note die IHK-Prüfung bestanden wurde.

# Link für die Bedingungen
# https://www.ihk.de/blueprint/servlet/resource/blob/5440118/9922dea3d1a2402026b5f361442799f5/neu-leitfaden-fisi-data.pdf
# Link für den Notenspiegel
# https://www.ihk.de/blueprint/servlet/resource/blob/2262812/3d0f9daa2673469ba4963b4097bdac5e/dezimaler-punkte-notenschluessel-data.pdf


# Das Zuweisen der Punktzahlen der Pruefungen
ap_1 = 50  # Abschlusspruefung Teil 1
ap_2_doku = 50  # Planen und Umsetzen eines Softwareprojektes die Dokumentation
ap_2_prae = 50  # Planen und Umsetzen eines Softwareprojektes die Praesentation und das Fachgespraech
ap_2_planen = 70  # Abschlusspruefung Teil 2 Planen eines Softwareproduktes
ap_2_entwick = 40  # Abschlusspruefung Teil 2 Entwicklung und Umsetzung von Algorithmen
wiso = 50  # Wirtschafts- und Sozialkunde

# Berechnung der Gesamtpunktzahl mit Gewichtung (.2 -> 20% gewichtung)
punkte = ap_1 * .2 + ap_2_doku * .25 + ap_2_prae * .25 + ap_2_entwick * .1 + ap_2_planen * .1 + wiso * .1

# Berechnung der Punktzahl fuer die AP2 mit Gewichtung (.2 -> 20% gewichtung)
punkte_teil2 = ap_2_doku * .25 + ap_2_prae * .25 + ap_2_entwick * .1 + ap_2_planen * .1 + wiso * .1

#  Ueber die Gesammt Punkte Entscheiden welche Note erreicht wurde
if punkte > 100:
	note = 'falsche'
elif punkte >= 92:
	note = 'sehr gut'
elif punkte >= 81:
	note = 'gut'
elif punkte >= 67:
	note = 'befriedigend'
elif punkte >= 50:
	note = 'ausreichend'
elif punkte >= 30:
	note = 'mangelhaft'
elif punkte >= 0:
	note = 'ungenügend'

# Ueberpruefen, ob die Leistung der AP2 ausreichend ist 40 punkte fuer ausreichent da 20 Punkte von der AP1 kommen

if punkte_teil2 < 50:
	print("Teil 2 nicht ausreichend")

# Ueberprufen, ob eine ungenuegende Leistung in der AP2 vorliegt

if wiso < 30 or ap_2_entwick < 30 or ap_2_planen < 30 or ((ap_2_doku + ap_2_prae) / 2) < 30:
	print("ungenuegende Leistung")

# Zaehlen der mangelhaften Leistungen der AP2 Pruefungen
mangelhaft = 0
if wiso < 50:
	mangelhaft += 1
if ap_2_planen < 50:
	mangelhaft += 1
if ap_2_entwick < 50:
	mangelhaft += 1
if ((ap_2_doku + ap_2_prae) / 2) < 50:
	mangelhaft = +1

# Bei zwei oder mehr mangelhafter Leistungen -> nicht bestanden
if mangelhaft >= 2:
	print('mangelhafte Leisungen')
print(note)

# 2 Variante mit verschachtelten If

#  Die Zuweisung der Punktzahlen der Pruefungen
ap1 = 50
ap2_doku = 50
ap2_praesi = 50
ap2_1 = 50
ap2_2 = 50
ap2_wiso = 50

# Gesamt Note des Projects
ap2_planen = (ap2_doku + ap2_praesi) / 2

# Berechnung der Gesamtpunktzahl mit Gewichtung (.2 -> 20% gewichtung)
punkte = ap1 * 0.2 + ap2_planen * 0.5 + ap2_1 * 0.1 + ap2_2 * 0.1 + ap2_wiso * 0.1


#  Ueber die Gesammt Punkte Entscheiden welche Note erreicht wurde

if punkte > 100:
	note = 'falsche'
elif punkte >= 92:
	note = 'sehr gut'
elif punkte >= 81:
	note = 'gut'
elif punkte >= 67:
	note = 'befriedigend'
elif punkte >= 50:
	note = 'ausreichend'
elif punkte >= 30:
	note = 'mangelhaft'
elif punkte >= 0:
	note = 'ungenügend'
# Ueberprufen, ob eine ungenuegende Leistung in der AP2 vorliegt

mangelhaft = 0
if ap2_planen < 30 or ap2_1 < 30 or ap2_2 < 30 or ap2_wiso < 30:
	print('ungenügende Leistung')
elif punkte < 50:
	print('gesamt unter 50%')
else:
	# Zaehlen der mangelhaften Leistungen der AP2 Pruefungen

	if ap2_1 < 50:
		mangelhaft += 1
	if ap2_2 < 50:
		mangelhaft += 1
	if ap2_wiso < 50:
		mangelhaft += 1
	if ap2_planen < 50:
		mangelhaft += 1

	if mangelhaft >= 2:
		print('mangelhafte Leistungen')
	else:
		print('Bestanden mit', punkte, note)



