
# Schreibe eine rekursive Funktion power(x, n), die die Potenz x hoch n berechnet.
# Schreibe eine rekursive Funktion reverse_string(s), die eine Zeichenkette s umkehrt.
# Schreibe eine rekursive Funktion is_palindrome(s), die überprüft, ob eine Zeichenkette s ein Palindrom ist.
def palindrom(wort):
	pali = True
	if len(wort) <= 1:
		print(f'pali{pali}')
		return True
	else:
		if wort[0] == wort[-1]:
			return palindrom(wort[1:-1])

		else:
			return False

print("qotto"[1:-1])

print(palindrom("otto"))
# Schreibe eine rekursive Funktion count_consonants(s), die die Anzahl der Konsonanten in einer Zeichenkette s zählt.
