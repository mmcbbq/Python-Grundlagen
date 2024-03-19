# Variablen die man in einer Funktion definiert stehen einem nur in der Funktion zur verfügung
# Scope einer Variable local oder global
# print(test) -> NameError: name 'test' is not defined
def hallo():
	var = "local"
	print(f'hallo{var}')


hallo()
# print(var) nur in der Funktion nutzbar

var = "global"
hallo()


def hallo_g():
	print(f'hallo_g:{var}')


hallo_g()


def hallo_innen():
	print(f'hallo_innen:{var}')


def hallo_aussen():
	var = "hallo_aussen"
	hallo_innen()
	print(var)


hallo_aussen()

print('-------------------ander der Uebergabe----------------')

liste = [1, 2, 3, 4, 5]
var_ubergabe = "Hallo"


def liste_func(vararg, l):
	global var_ubergabe
	var_ubergabe = vararg
	vararg = vararg + "liste_func"
	l.append("sechs")
	print(f"func var:{var} liste:{l}")


liste_func("var_ubergabe", liste)
print(var_ubergabe, liste)
