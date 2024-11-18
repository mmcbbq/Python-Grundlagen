# Falsy
falsy = {
	'lists': [],
	'dictionaries': {},
	'tuples': (),
	'sets': set(),
	'strings': ' ',
	'integer': 0,
	'floats': 0.0,
	'none': None,
	'bools': False
}

truthy = {
	'lists': [0],
	'dictionaries': {'key': 0},
	'tuples': (0),
	'sets': set({0}),
	'strings': '0',
	'integer': 1,
	'floats': 1.0,
	'bools': True}


for key, val in falsy.items():
	if not val:
		print(f'{key}: {val} -> false')
	else:
		print(f'{key}: {val} -> True')


print('-----------------------')
print('-----------------------')
print('-----------------------')
for key, val in truthy.items():
	if val:
		print(f'{key}: {val} -> True')