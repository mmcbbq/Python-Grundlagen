# Alte Methoden um Strings zu Formatieren

name = 'Bob'
alter = 22
print('Hallo mein name ist %s und ich bin %s <- sehr alt' % (name, alter))

print('Hallo mein name ist {} und ich bin {} <- alt'.format(name, alter))
# Modern ist die F.Sting Methode
# https://docs.python.org/3/library/string.html#format-specification-mini-language
# https://mkaz.blog/working-with-python/string-formatting/
print(f"Hallo mein Name ist {name} und ich bin {alter}")


# Operationen durchführen
print(f'Ich bin {80-alter} Jahre alt')
print(f'Ich bin {80 == alter} Jahre alt')

zahl = 1010025562002.536895514
print(f'Die Zahl ist {zahl:.2f}')

