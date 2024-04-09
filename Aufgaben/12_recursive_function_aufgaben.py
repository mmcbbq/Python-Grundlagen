# Schreibe eine rekursive Funktion power(x, n), die die Potenz x hoch n berechnet.

def power(x, n):
	if n == 1:
		return x
	else:
		return x * power(x, n - 1)


print(power(3, 3))

# return 2 ** power(3, 1)
#
# return 3 ** power(1, 2)
#
# return 1 ** power(2,0)
# return 1
#
# return 1
# return 3
# return 2 3 ->

# Schreibe eine rekursive Funktion reverse_string(s), die eine Zeichenkette s umkehrt.

def reverse_string(s):
	if s == "":
		return s
	else:
		return s[-1] + reverse_string(s[:-1])


print(reverse_string("test"))



# Schreibe eine rekursive Funktion is_palindrome(s), die überprüft, ob eine Zeichenkette s ein Palindrom ist.


def is_palindrome(string, index=0):
    if index <= len(string) // 2:
        return string[index].lower() == string[len(string) - 1 - index].lower() and is_palindrome(string, index + 1)
    else:
        return True


print(is_palindrome('Anna'))



# Schreibe eine rekursive Funktion count_consonants(s), die die Anzahl der Konsonanten in einer Zeichenkette s zählt.

def count_consonants(s):
	vokale = "aeiou"
	s = s.lower()
	if s == "":
		return 0
	else:

		if s[0] not in vokale:

			return 1 + count_consonants(s[1:])
		else:
			return count_consonants(s[1:])