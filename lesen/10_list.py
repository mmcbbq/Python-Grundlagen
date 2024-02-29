my_list = [50, 50.55, 'string', True]
print(type(my_list))  # -> <class 'list'>
# Anzahl der itmes in der Liste

print(len(my_list))  # -> 4
print(my_list.count('string'))  # -> zählt die Anzahl der Elemente


# leere Liste
leere_liste = []

# List Constructor
con_list = list((50, 50, 50, True, 'string'))

my_list = [50, 50.55, 'string', True]
# Auswahl von List Items
print(my_list[0])  # -> 50
print(my_list[3])  # -> True
print(my_list[-1])  # -> True
print(my_list[1:3])  # -> 50.55, 'string' in einer neuen Liste
print(my_list[:3])  # -> 50, 50.55, 'string'
print(my_list[2:])  # -> 'string', True
print(my_list[-4:-1])  # -> 50, 50.55, 'string'

# Change
my_list = [50, 50.55, 'string', True]
my_list[-1] = False
my_list[2] = my_list[2][0].upper() + my_list[2][1:]
print(my_list)
my_list[0:2] = [80, 95.5]
print(my_list)

# hinzufügen
my_list = [50, 50.55, 'string', True]
my_list.append('ganz hinten')
print(my_list)
my_list.insert(1, 50.25)
print(my_list)
my_list2 = [5, 6, 7, 8, 9]

# Eine Liste einer anderen anhängen
# my_list.append(my_list2) #-> geht nicht verschachtelt die Listen
# print(my_list)
my_list.extend(my_list2)  # -> extend geht
# my_list = my_list + my_list2 # -> das addieren geht auch
print(my_list)

# Remove
my_list = [50, 50.55, 'string', True]

my_list.pop()  # -> entfernt das letzte Element einer Liste

my_list.pop(1)  # -> um ein Element an einer bestimmten stellen zu entfernen kann man pop ein Index als arg übergeben
print(my_list)
my_list.remove('string')  # -> remove entfernt ein Element das == des Übergabeparameters ist
print(my_list)
my_list = [50, 50.55, 'string', True, 'string']
my_list.remove('string')  # -> entfernt nur ein Element. Entfernt das mit dem kleinsten positiven index
print(my_list)

my_list = [50, 50.55, 'string', True]

del my_list[0]  # -> entfernt das Element mit dem Index 0

print(my_list)
# del my_list -> löscht die gesamte Liste
print(my_list)
my_list.clear()  # -> löscht den Inhalt der Liste
print(my_list)

my_list = [50, 50.55, 'string', True]

my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)
z = my_list[0]
my_list[0] = my_list[-1]
my_list[-1] = z
print(my_list)

print(50 in my_list)  # -> mit den in operator kann man nach Elementen in der Liste suchen
print(51 in my_list)

my_list = [50, 50.55, 'string', True]



my_list_copy = my_list
print(my_list)
print(my_list_copy, 'copy')
my_list.pop()
print(my_list)
print(my_list_copy, 'copy')
print('#########################')
my_list = [50, 50.55, 'string', True]






my_list_copy = my_list.copy()
my_list.pop()
print(my_list)
print(my_list_copy, 'copy')

my_list_copy = list(my_list)  # -> das gleiche Ergebnis wie mit Copy

# https://www.w3schools.com/python/python_lists_methods.asp
# - append()   # slicing ?
# - pop()
# - remove()
# - count()
# - sort()
# - reverse()
# - extend()
# - clear()
# - index()
# - insert()