# In Python können wir eine Variable definieren und einen Wert zuweisen.
# Der Datentype der Variable bestimmt Python "Duck Typing"
#
my_var = "Hello World"
print(type(my_var))
my_var = 15
print(type(my_var))
my_var = 15.5
print(type(my_var))
my_var = True
print(type(my_var))
print()
print()
print()
print()
print()
print()

zahl = "aasd"
print('String: ', type(zahl), zahl)
print(zahl * 3)
zahl = int(zahl)
print('Int:', type(zahl), zahl)

zahl = float(zahl)
print('Float:', type(zahl), zahl)

zahl = str(zahl)
print('String: ', type(zahl), zahl)

zahl = -10.9
zahl = int(zahl)
print(zahl)

# ------type check----


int_var = 12
str_var = 'test'
float_var = 12.334
bool_var = True

print(type(int_var) is int)
print(type(str_var) is str)
print(type(float_var) is float)
print(type(bool_var) is bool)
