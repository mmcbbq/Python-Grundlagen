
opt = int(input('bin to oct(1) oct to bin'))

zahl = input('wert')
if opt == 1:
	txt = 'Oktalzahl'
	zahl = oct(int(zahl, 2))
elif opt == 2:
	txt = 'Bin'
	zahl = bin(int(zahl,8))
print(txt,str(zahl)[2:])


