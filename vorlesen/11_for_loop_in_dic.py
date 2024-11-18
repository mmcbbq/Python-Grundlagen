# Um durch die Keys des Dictionary's zu iteriren

my_dic = {"string": "wert1", "int": 50, "float": 10.2, "bool": True}
print('------- keys --------')
for key in my_dic:
    print(key)
print('------- keys methode--------')

for key in my_dic.keys():
    print(key)

# Um die Values zu erhalten
print('------- values ueber den Key --------')

for key in my_dic:
    print(my_dic[key])

# oder mit der values methode
print('------- values mit der values methode --------')

for val in my_dic.values():
    print(val)

# mit der Items methode kann man eine Schleife variable fuer die Keys und die Values

for key, val in my_dic.items():
    print(f"{key}:{val}")
