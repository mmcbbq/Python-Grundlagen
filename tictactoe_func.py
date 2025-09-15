def show_game(field):
	print(field[2])
	print(field[1])
	print(field[0])


def ask_move():
	x = int(input("x: 123"))
	y = int(input("y: 123"))
	return x - 1, y - 1


def check_move(feld, move, spieler):
	if feld[move[0]][move[1]] == spieler[0]['zeichen'] or feld[move[0]][move[1]] == spieler[1]['zeichen']:
		return False
	return True


def set_move(feld, move, spieler):
	feld[move[0]][move[1]] = spieler['zeichen']


def switch_player(player_now, player):
	if player_now == player[1]:
		return player[0]
	else:
		return player[1]