# Boolean values sind entweder Wahr True oder Falsch False

wahr = True
falsch = False

# Vergleich Operatoren
# ==
print("==")
print('----------------------------------------')
print(15 == 15)  # True
print(15 == 20)  # False
print(15 == 15.)  # True
print(15 == "15")  # False
print('15' == '15')  # True
print('15' == 'fünfzehen')  # False

# !=
print("!=")
print('----------------------------------------')
print(15 != 15)  # False
print(15 != 20)  # True
print(15 != 15.)  # False
print(15 != "15")  # True
print('15' != '15')  # False
print('15' != 'fünfzehen')  # True
# <
print("<")
print('----------------------------------------')
print(15 < 15)  # False
print(15 < 20)  # True
print(15 < 10)  # False
print(-15 < -20)  # False
print(-15 < -10)  # True

print(">")
print('----------------------------------------')
print(15 > 15)  # False
print(15 > 20)  # Fasle
print(15 > 10)  # True
print(-15 > -20)  # True
print(-15 > -10)  # False

print(">=")
print('----------------------------------------')
print(15 >= 15)  # True
print(15 >= 20)  # Fasle
print(15 >= 10)  # True
print(-15 >= -20)  # True
print(-15 >= -10)  # False

print("<=")
print('----------------------------------------')
print(15 <= 15)  # True
print(15 <= 20)  # True
print(15 <= 10)  # False
print(-15 <= -20)  # False
print(-15 <= -10)  # True

# Membership
# in
print('in')
print('----------------------------------')

print('Hallo' in "Hallo Welt")  # True
print('Hallo Welt' in "Hallo")  # False
print('hallo' in "Hallo Welt")  # False

# not in
print('not in')
print('----------------------------------')

print('Hallo' not in "Hallo Welt")  # False
print('Hallo Welt' not in "Hallo")  # True
print('hallo' not in "Hallo Welt")  # True

# and or xor

print('--------and or xor-------------------------')
print(' and')

print('True and True:', True and True)
print('True and False:', True and False)
print('False and False:', False and False)

print('or')

print('True or True:', True or True)
print('True or False:', True or False)
print('False or False:', False or False)

print('xor')

print('True xor True:', True ^ True)
print('True xor False:', True ^ False)
print('False xor False:', False ^ False)

# xor kann man logisch aus den anderen Operatoren zusammen setzten
print('xor aus and und or')
a = True
b = True

print('True xor True:', (a and not b) or (not a and b))
a = True
b = False
print('True xor False:', (a and not b) or (not a and b))
a = False
b = False
print('False xor False:', (a and not b) or (not a and b))

