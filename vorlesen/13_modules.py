# module sind einzelne python files
#
# packages sind mehrere files

# es gibt interne und externe module und pakete
# interne sind im Python interpreter gespeichert
# externe muessen installiert werde pip oder selbst geschrieben werden

# wie findet der interpreter diese Dateien?
import sys

print(f'Pathvariable')
for x in sys.path:
    print(x)
print('-----------------------------')
print('-----------------------------')
print('-----------------------------')

# es gibt wieder eine Pathvariable enthaelt
# Project dir
# current dir pip
# install dir
# dir fuer OS kommunikation


# Wenn wir eine eignes module erstellen module_import


import module_import

print('path from module import wie type oder whereis in Linux')
print(f"Hier ist {module_import.__file__}")
print('-----------------------------')
print('-----------------------------')
print('-----------------------------')

# um die var und func zu nutzen
print('Nutzten des Modules')
print(module_import.var)
module_import.hallo_name("Joe")
print('-----------------------------')
print('-----------------------------')
print('-----------------------------')

# installieren eine

from faker import Faker

# print(Faker.__file__)
# pip freeze
# pip install faker
# pip freeze > requirements.txt
#pip install -r requirements.txt
fake = Faker('de_DE')
for x in range(1, 100):
    print(fake.name())
