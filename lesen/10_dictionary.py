my_dic = {"string": "wert1", "int": 50, "float": 10.2, "bool": True}
print('type')
print(type(my_dic))  # type dict
print('laenge')
print(len(my_dic))

# leere dic
leeres_dic = {}
# dic mit Constructor
print("constructor")
con_dic = dict()
print(type(con_dic))

my_dic = {"string": "wert", "int": 50, "float": 10.2, "bool": True}
# Auswahl von Items
print("Auswahl")
print(my_dic['string'])
print(my_dic.get("string"))
print(my_dic["bool"])
# Sliceing import itertools

# Die keys() methode gibt eine liste alles keys
print("keys")
print(my_dic.keys())
# Die values() methode gibt eine liste alles werte
print('values')
print(my_dic.values())

# Change
my_dic["string"] = "change"
print('change wert zu change')
print(my_dic)

# oder update()
print('change wert zu update mit update')
my_dic.update({"string": "update"})
print(my_dic)

# add
print('add string_neu : change')
my_dic["string_neu"] = "change"
print(my_dic)

# oder update()
print('add string_update : update')

my_dic.update({"string_update": "update"})
print(my_dic)

# remove mit pop(key)

my_dic.pop('string_neu')
print('remove string_neu pair mit pop()')
print(my_dic)

# remove last item .popitem
my_dic.popitem()
print('remove last pair mit popitem')

print(my_dic)

# del zum Entfernen eines Items
print('remove string pair mit del keyword')
del my_dic["string"]
print(my_dic)
# oder zum loeschen des dic
print('delete my_dic mit del keyword')
del my_dic
# print(my_dic)

# clear um es zu leeren
my_dic = {"string": "wert", "int": 50, "float": 10.2, "bool": True}
my_dic.clear()
print('leeren des dic mit clear')
print(my_dic)



my_dic = {"string": "wert", "int": 50, "float": 10.2, "bool": True}


print('-------------my_dic = my_dic2')
my_dic2 = my_dic
print('my_dic')
print(my_dic)
print('copy')
print(my_dic2)

my_dic.clear()


print('nach mydic.clear')
print('my_dic')
print(my_dic)
print('copy')
print(my_dic2)

print('-------------copy------------------------------------')


my_dic2 = my_dic.copy()
print('my_dic')
print(my_dic)
print('copy')
print(my_dic2)

my_dic.clear()


print('nach mydic.clear')
print('my_dic')
print(my_dic)
print('copy')
print(my_dic2)