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
print('###########################################################')
print('###########################################################')
print('###########################################################')
print('###########################################################')
print('hallo_g')


def hallo_g():
	print(f'hallo_g:{var}')


hallo_g()

print('###########################################################')
print('###########################################################')
print('###########################################################')
print('###########################################################')
print('hallo_innen aussen')


def hallo_innen():
	print(f'hallo_innen:{var}')


def hallo_aussen():
	var = "hallo_aussen"
	hallo_innen()
	print(f'hallo_aussen{var}')


print('call hallo_aussen')
hallo_aussen()


def hallo_innen_global():
	global var

	print(f'hallo_innen:{var}')


def hallo_aussen():
	var = "hallo_aussen"
	hallo_innen_global()
	print(f'hallo_aussen{var}')


print('call hallo_aussen innenglobal')
hallo_aussen()

print('global Keyword')


def erstelle_var(var2):
	global new_global
	new_global = var2


erstelle_var(123)
print(new_global)

print('-------------------anderern der Uebergabe----------------')

liste_ubergabe = ["alt", 2, 3, 4, 5]
var_ubergabe = "alt"


def change_string(string):
	string = "new"


def change_liste(liste):
	liste[0] = 'new'


change_string(var_ubergabe)
print(var_ubergabe)
change_liste(liste_ubergabe)
print(liste_ubergabe)