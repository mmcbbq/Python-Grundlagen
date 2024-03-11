dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
new_dict = {}
for key in dict1:
	if key in dict2:
		new_dict[key] = dict1[key] + dict2[key]
print(new_dict)