# Sommer 2022 Ap1
PCNr = 1
SoftwareNr = 1


# PcListe = []
# SoftwareListe = []


def getPC():
	return ['Pc1', 'Pc2', 'Pc3', 'Pc4', 'Pc5', 'Pc6']


def getSoftware(pc):
	if True:
		pass
	return ['Word', 'Teams', 'Powerpoint', 'Excel']


def installSoftware(software, pc):
	print(f'{software} auf {pc} installiert')


# PcListe = getPC()
# for pc in PcListe:
# 	SoftwareListe = getSoftware(pc)
# 	for software in SoftwareListe:
# 		installSoftware(software, pc)
# 		SoftwareListe = []

# mit while

# PcListe = getPC()  # Zeile 3
# PCNr = 0  # Zeile 5 Start index
# while PCNr < len(PcListe):  # Zeile 9
# 	SoftwareListe = getSoftware(PcListe[PCNr])  # Zeile 6
# 	SoftwareNr = 0  # Zeile 7
# 	while SoftwareNr < len(SoftwareListe):  # Zeile 2
# 		installSoftware(SoftwareListe[SoftwareNr], PcListe[PCNr])  # Zeile 1
# 		SoftwareNr = SoftwareNr + 1  # Zeile 8  -> ++ SoftwareNr
# 	PCNr += 1  # Zeile 4 -> ++ PCNr

# mit range

PcListe = getPC()  # Zeile 3

for PCNr in range(0, len(PcListe),
				  1):  # Zeile 5 9 und 4 -> andere schreibweise     for int PCNr = 0 , PCNr <= PCListe.len()-1 ,  PCNr ++
	SoftwareListe = getSoftware(PcListe[PCNr])  # Zeile 6
	for SoftwareNr in range(0, len(SoftwareListe), 1):  # Zeile 2, 7 und 8
		installSoftware(SoftwareListe[SoftwareNr], PcListe[PCNr])  # Zeile 1


# -----------------------------------------------------------------------
# Herbst 2022 Ap1
def setRollerDim(breite, länge, dicke):
	print(f"{breite}, {länge} und {dicke} eingestellt")


def getEmergencyStop():
	return False


def rollerStart():
	print(f'Wellpappe erstellt')


# def launchTask(result):
# 	setRollerDim(result[0], result[1], result[2])
# 	i = 0
# 	while i < result[3] and not getEmergencyStop():
# 		rollerStart()
# 		i += 1

def launchTask(result):  # Zeile 1  result[]
	i = 0  # Zeile 2   int i = 0
	emergencyStop = getEmergencyStop()  # Zeile 3 bool emergencyStop
	setRollerDim(result[0], result[1], result[2])  # Zeile 4
	while i < result[3] and emergencyStop == False:  # Zeile 5
		rollerStart()  # Zeile 6
		i = i + 1  # Zeile 7  -> i++ oder i+=1
		emergencyStop = getEmergencyStop()  # Zeile 8


launchTask([3, 4, 5, 6])
# # --------------------------------------------------
# # Sommer Ap2-1
werte = [30, 24, 12, 50, 11, 49, 11]  # Beispeil Werte
temp = None
len_list = len(werte)  # Länge des arrays
for p in range(0, len_list - 1, 1):  # äußere Schleife   for (int p = 0; p <= len_list - 2; p++){
	for i in range(0, len_list - 1 - p, 1):  # innere Schleife for( int i = 0; i <= len_list -2 - p ; i++){
		if werte[i] > werte[i + 1]:  # Vergleich  if (werte[i] > werte[i + 1]){
			temp = werte[i]  # tausch
			werte[i] = werte[i + 1]  # tausch
			werte[i + 1] = temp  # tausch
								# 		} Ende des Vergleichs
								#  	} Ende der inneren Schleife
								#  } Ende der äußeren Schleife
print(werte)

