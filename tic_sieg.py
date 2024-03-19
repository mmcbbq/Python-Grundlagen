def sieg_waage(nested_list):
	for liste in nested_list:
		if liste[0] == liste[1] and liste[0] == liste[2] and liste[0] != '-':
			return True
	return False


# senkrechter Sieg
def sieg_senk(nested_list):
	for x in range(3):
		if nested_list[0][x] == nested_list[1][x] == nested_list[2][x] != '-':
			return True
	return False


def sieg_diag_ol_ur(nested_list):
	if nested_list[0][0] == nested_list[1][1] == nested_list[2][2] and nested_list[0][2] != "-":
		return True
	else:
		return False


def sieg_diag_or_ul(nested_list):
	if nested_list[0][2] == nested_list[1][1] == nested_list[2][0] and nested_list[0][2] != "-":
		return True
	else:
		return False