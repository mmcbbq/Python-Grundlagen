# while True:
# 	print("Hallo Welt")

n = 10
while n > 0:
	print(n)
	n -= 1

ant = input("Soll das Programm geschlossen werden? y n")

while ant != "y":
	print("Funktion")
	ant = input("Soll das Programm geschlossen werden? y n")

x = 50

while x > 0:
	print(x)
	x -= 1
	if x == 25:
		break
print("###########################################")
while x > 0:
	x -= 1
	if x == 10:
		continue
	print(x)

my_list = ["Bob","Tim","Tom", "Alice"]
x = 0
name = my_list[x]

while name != "Tim":
	print("Kein Treffer", name)
	x += 1
	name = my_list[x]
print(f"Der {name} hat den index {x}")


liste = [1,2,3]

for x in liste:
	liste.append(x)
	print(x)