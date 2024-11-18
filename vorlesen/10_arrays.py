# In Python gibt es keine "Arrays".

# List -> indexed array geordnet änderbar erlaubt duplicate []
# Tuple -> indexed array geordnet nicht änderbar duplicate ()
# Set -> ungeordnet nicht änderbar keine duplicate {}
# Dictionary-> associative key value pair geordnet änderbar keine duplicate {}

my_list = [50, 60, 50, 50, 40, 50]
my_tuple = (50, 60, 50, 50, 40, 50)
my_set = {50, 60, 50, 50, 40, 50}
my_dic = {'ap1': 50, 'ap2_doku': 60, 'ap2_prasi': 50, 'ap2_1': 50, 'ap2_2': 40, 'ap2_wiso': 50, 'ap1': 80}
# geordnet und duplicate
print("--------geordnet un duplicate-------------")
print(my_list)
print(my_tuple)
print(my_set)
print(my_dic)
# aenderbar man kann die items der "arrays" aendern  oder nicht
my_list[0] = 70  # aenderbar
# my_tuple[0] = 70  # nicht aenderbar
# my_set[0] = 70  # nicht aenderbar
my_dic["ap1"] = 70  # aenderbar
print("---------aenderbar------------")
print(my_list)
print(my_tuple)
print(my_set)
print(my_dic)
# aenderbar bezieht sich nur auf die items des "arrays" ob man items hinzufuegen oder entfernen
# kann ist eine andere Sache
my_list.append(80)  # aenderbar
# my_tuple.append(80)  # nicht aenderbar
my_set.add(90)  # aenderbar
my_dic["hinzu"] = 100  # aenderbar
print("----------hinzu-----------")
print(my_list)
print(my_tuple)
print(my_set)
print(my_dic)

my_list.pop()  # aenderbar
# my_tuple.pop()  # nicht aenderbar
my_set.remove(90)  # nicht aenderbar
my_dic.pop("hinzu")  # aenderbar
print("--------enfernen-------------")
print(my_list)
print(my_tuple)
print(my_set)
print(my_dic)
