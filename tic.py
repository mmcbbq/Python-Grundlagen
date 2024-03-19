from tic_sieg import *
from tic_func import *


spielfeld = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
spieler = 'x'
while True:
	print_spielfeld(spielfeld)
	print(f'Spieler {spieler} am Zug')
	setzte_feld(spielfeld, spieler)
	if sieg_waage(spielfeld) or sieg_senk(spielfeld) or sieg_diag_or_ul(spielfeld) or sieg_diag_ol_ur(spielfeld):
		print(f'Spieler {spieler} hat gewonnen')
		print_spielfeld(spielfeld)
		break
	elif spieler == 'x':
		spieler = 'o'
	elif spieler == 'o':
		spieler = 'x'