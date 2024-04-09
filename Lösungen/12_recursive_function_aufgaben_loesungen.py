# Schreibe eine rekursive Funktion power(x, n), die die Potenz x hoch n berechnet.

def power(x, n):
	if n == 1:
		return x
	return x * power(x, n - 1)


# power(3,3) return x * power(3,2)
# power(3,2) return x * power(3,1)
# power(3,1) return x

# power(3,2) return x * x
# power(3,3) return x * x * x
print(power(2, 8))


# Schreibe eine rekursive Funktion reverse_string(s), die eine Zeichenkette s umkehrt.

def reverse_string(s):
	if len(s) == 1:
		return s
	else:
		return reverse_string(s[1:]) + s[0]


my_string = ""
print(my_string[1:])
# print(reverse_string(my_string))


# Schreibe eine rekursive Funktion is_palindrome(s), die überprüft, ob eine Zeichenkette s ein Palindrom ist.
def palindrom(wort):
	if len(wort) <= 1:
		return True
	else:
		if wort[0] == wort[-1]:
			return palindrom(wort[1:-1])

		else:
			return False


print('ist palindrome',palindrom("ot1ato"))


# Schreibe eine rekursive Funktion count_consonants(s), die die Anzahl der Konsonanten in einer Zeichenkette s zählt.

def count_consonants(s):
	if len(s) == 0:
		return 0

	elif s[0] in 'aeiou':
		return 0 + count_consonants(s[1:])
	else:
		return 1 + count_consonants(s[1:])


print(count_consonants("abcdef"))
