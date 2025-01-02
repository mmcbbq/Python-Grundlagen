zahl1 = int(input("Zahl1"))
zahl2 = int(input("Zahl2"))
zahl3 = int(input("Zahl3"))

if zahl1 > zahl2:
    if zahl1 > zahl3:
        print(f"Zahl1 {zahl1} ist > als {zahl2} und {zahl3}")
elif zahl2 > zahl3:
    print(f"Zahl1 {zahl2} ist > als {zahl1} und {zahl3}")
else:
    print(zahl3)

if zahl1 > zahl2 and zahl1 > zahl3:
    print('zahl1')
elif zahl2 > zahl1 and zahl2 > zahl3:
    print("zahl2")
elif zahl3 > zahl1 and zahl3 > zahl2:
    print("zahl3")
