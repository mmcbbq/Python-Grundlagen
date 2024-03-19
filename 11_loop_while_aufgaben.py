
import random

zufall_zahl = random.randint(1, 100)
count = 0
while True:
	count += 1
	eingabe = int(input("Deine Zahl?"))
	if eingabe > zufall_zahl:
		print("Das war zu gross")
	elif eingabe < zufall_zahl:
		print("Das war zu klein")
	else:
		print(f"Ja richtig die Zahl war {zufall_zahl} versuch {count}")
		break