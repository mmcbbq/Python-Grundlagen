# floats sind kommazahlen

zahl1 = 2.5  # positive
zahl2 = - 0.55  # negative

zahl3 = +1.55
zahl = 0.123
zahl5 = .123  # gleicher wert wie in Zeile 8

zahl4 = 4.  # auch ein float
print(zahl4)
print(5e10)  # 10 potenz gibt immer float

print("*")
print("-------------------------------------")
print(2 * 3)  # int
print(2 * 3.)  # float
print(2. * 3)  # float
print(2. * 3.)  # float
print("/")
print("-------------------------------------")
print(6 / 3)  # float
print(6 / 4.)  # float
print(6. / 4)  # float
print(6. / 4.)  # float
print("//")
print("-------------------------------------")
print(6 // 4)  # int
print(6 // 4.)  # float
print(6. // 4)  # float
print(6. // 4.)  # float
print("-/")
print("-------------------------------------")
print(-6 // 4)  # int
print(-6 // 4.)  # float
print(-6. // 4)  # float
print(-6. // 4.)  # float

print('----------------------------------------')
# Bei float auf rundungsfehler achten!!!!
print(15.2 - 11)
# Besser mal 10 ** x nehmen, um mit int zu arbeiten
print(((15.2 * 10) - (11 * 10)) / 10)
