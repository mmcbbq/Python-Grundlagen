#    a     b     c
#       |     |
# 3  -  |  -  |  -
#  _____|_____|_____
#       |     |
# 2  -  |  -  |  -
#  _____|_____|_____
#       |     |
# 1  -  |  -  |  -
#       |     |
spielfeld = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
spieler = [{'name': input(('name spieler 1')), 'zeichen': input("zeichen spieler 1")},
		   {'name': input(('name spieler 2')), 'zeichen': input("zeichen spieler 2")}]




aktueller_spieler = spieler[1]
def show_game(field):
	print(f'y3{field[2]}')
	print(f'y2{field[1]}')
	print(f'y1{field[0]}')
	print(f'\tx1 \t x2    x3')


def ask_move():
	x = int(input('x 1 2 3 ?'))
	y = int(input('y 1 2 3 ?'))
	return x - 1, y - 1


def check_move(move, feld):  # -> {2,1}
	if feld[move[1]][move[0]] == "-":
		return True
	else:
		return False


def set_move(feld, move, zeichen):
	feld[move[1]][move[0]] = zeichen


def sieg_w(feld):
	for inner_list in feld:
		if inner_list[0] == inner_list[1] and inner_list[0] == inner_list[2] and inner_list[0] != '-':
			return True
	return False


def sieg_s(feld):
	for x in range(3):
		if feld[0][x] == feld[1][x] and feld[0][x] == feld[2][x] and feld[0][x] != "-":
			return True
	return False


def sieg_dlr(feld):
	if feld[0][0] == feld[1][1] and feld[0][0] == feld[2][2] and feld[0][0] != "-":
		return True
	return False


def sieg_drl(feld):
	if feld[0][2] == feld[1][1] and feld[0][2] == feld[2][0] and feld[1][1] != "-":
		return True
	return False


def sieg(feld):
	if sieg_w(feld) or sieg_s(feld) or sieg_dlr(feld) or sieg_drl(feld):
		return True
	else:
		return False


def switch_player(player_now,player):
	if player_now == player[0]:
		return player[1]
	else:
		return player[0]


gewonnen = False
show_game(spielfeld)
while not gewonnen:
	print(f'Spieler {aktueller_spieler["name"]} ist am Zug')
	move = ask_move()
	while not check_move(move, spielfeld):
		print("Das geht nicht")
		move = ask_move()

	set_move(spielfeld, move, aktueller_spieler['zeichen'])
	show_game(spielfeld)
	gewonnen = sieg(spielfeld)
	aktueller_spieler = switch_player(aktueller_spieler, spieler)


aktueller_spieler = switch_player(aktueller_spieler, spieler)
print(f'{aktueller_spieler["name"]} hat gewonnen')