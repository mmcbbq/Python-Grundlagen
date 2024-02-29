# nested list oder multidimensional array. Listen die Listen enthalten
nested_list = [1, 2, 3, 'a', 'b', 'c', True, False, True, [1, 2, 3], ['a', 'b', 'c'],
			   [True, False, True, [1, 'b', False]]]

print(nested_list[9])  # -> innere Listen kann ansprechen in dem ich zunächst die äussere Liste anpreche und auf den Index mit der inneren Liste verweise
print(nested_list[9][1])  # -> die Elemente der inneren Liste kann man wieder mit den Index ansprechen
print(nested_list[10][0])
print(nested_list[11][-1])
print(nested_list[11][-1][1])

nested_list[10].append('d')  # -> man kann auch alle Listen methoden auf die inneren Listen anwenden
print(nested_list[10])
nested_list[11].insert(0, 'bool')
nested_list[11][1] = False
nested_list[11][-1].pop(-2)
# nested_list.remove('b') #-> Findet keine Elemente der inneren Liste
# nested_list.remove(['a','b','c','d']) #-> aber remove kann innere Listen entfernen
if ['a', 'b', 'c'] == ['a', 'b', 'c']:  # -> Listen mit gleichen Inhalten ergeben == True
	print('True')
else:
	print('False')

nested_list[10].extend(1)
print(nested_list)
