# Ein integer ist eine ganze Zahl
zahl = 123
# Es können auch negative Zahlen sein
zahl_negativ = -123
# man kann auch ein plus vor positiven schreiben ist aber nicht nötig
zahl2 = +123
# lange zahlen kann man zur Besseren lesbarkeit mit _ versehen
lange_zahl = 1_550_048_766_540

# mit int können alle mathematician Operatoren verwendet werden
# addition
plus = zahl + zahl2
print(plus)
# subtraktion
minus = zahl - zahl2
print(minus)
#  multiplikation
mul = zahl * zahl2
print(mul)
#  division
div = 100 / 3
print(div)  # bei der Division erhält man als Ergebnis IMMER einen Float

# mit der floor division erhält man immer einen int es werden aber immer abgerundet
floor_div = zahl // zahl2
print(floor_div)
# Bei negativen Zahlen rundet floor auf die kleine Zahl also die Negativ Größere
print('floor Negativ', -10 // 3)
a = 10
b = 4
c = 3
# exponential Rechnung mit **
print(b ** c)
# bei der exponential Rechnung von Rechtspotenz nach links
# Möglichkeit 1. 2 ** 2 -> 4 -> 4 ** 4 -> 64 links nach rechts FALSCH
# Möglichkeit 2. 2 ** 3 -> 8 -> 2 ** 8 -> 265 rechts nach links RICHTIG
print(2 ** 2 ** 3)

# Zur Wurzel berechnung entweder über das Importieren der Math
import math

print(math.sqrt(16))
# Oder mithilfe der Potenzgesetze
print("mit Potenz", 27 ** (1 / 3))

# modulo
print(10 % 3)
# 10 // 3 -> 3
# 3 * 3 -> 9
# 10 - 9 -> Endergebnis 1
print(13 % 5)
# 13 // 5 -> 2
# 5 * 2 -> 10
# 13 - 10 -> 3
print(10 % 2)
# 10 // 2 -> 5
# 5 * 2 -> 10
# 10 - 10 -> 0

# Binäre
binaere = 0b1010
print(binaere)
dez = 256
print(bin(dez))
# Oktal
oktal = 0o755
print(oktal)
print(oct(dez))
# Hex
hexa = 0xfff
print(hexa)
print(hex(dez))


# and & , oder | , xor ^ , not ~
x = 0b101010110011
y = 0b010011010100
print('-------------------------------------------')
print(bin(x & y))  # 10010000
#                    10010000

print(bin(x | y))  # 111011110111

print(bin(x ^ y))  # 111001100111


# 0b101010110011

print('-------------------------')
print('~')

x = 2 # 0000 0010
print(bin(x))
x =~2 # 1111 1101 -> -0b11
print(bin(x))
x -2 # 1111 0010 -> +1bit -> 00 11 -> -0b11
print(bin(x))



print('<<')
a = 0b1100
a = a >> 1
print(bin(a))

b = 0b1100

print(a << 3)
print(a >> 3)

