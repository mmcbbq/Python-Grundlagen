# Erstelle ein leeres Dictionary namens my_dict.
my_dict = {}
# Fülle das Dictionary my_dict mit drei Schlüssel-Wert-Paaren:
# "Apfel" mit dem Wert 3, "Banane" mit dem Wert 2 und "Orange" mit dem Wert 5.
my_dict["Apfel"], my_dict['Banane'], my_dict['Orange'] = 3, 2, 5

print(my_dict)

# Drucke den Wert für den Schlüssel "Banane" aus.
print(my_dict["Banane"])
# Überprüfe, ob der Schlüssel "Traube" im Dictionary my_dict vorhanden ist.
print("Traube" in my_dict)
# Füge dem Dictionary my_dict einen neuen Eintrag hinzu: "Traube" mit dem Wert 4.
my_dict["Traube"] = 4
print(my_dict)

# Aktualisiere den Wert für den Schlüssel "Apfel" auf 6.
my_dict['Apfel'] = 6
print(my_dict)

# Lösche den Eintrag für den Schlüssel "Orange" aus dem Dictionary.
# del my_dict['Orange']
my_dict.pop('Orange')
print(my_dict)

# Drucke alle Schlüssel in my_dict aus.
print(my_dict.keys())
# Drucke alle Werte in my_dict aus.
print(my_dict.values())
# Drucke alle Schlüssel-Wert-Paare in my_dict aus
print(my_dict.items())