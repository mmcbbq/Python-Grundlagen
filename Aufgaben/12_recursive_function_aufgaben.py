# Schreibe eine rekursive Funktion power(x, n), die die Potenz x hoch n berechnet.
def pow(x: int, n: int) -> int:
    pass


# Schreibe eine rekursive Funktion, die Summe aller Zahlen in einer gegebenen Liste berechnet

list_sum = [12, 13, 14, 15]

def summe_rec(l: list) -> int:
    pass

# Schreibe eine rekursive Funktion, die die Fakultät einer Zahl n berechnet.
def faku(n: int) -> int:
    pass

# Schreibe eine rekursive Funktion reverse_string(s), die eine Zeichenkette s umkehrt.

def reverse_string(s: str) -> str:
    pass







# Schreibe eine rekursive Funktion is_palindrome(s), die überprüft, ob eine Zeichenkette s ein Palindrom ist.

def is_palindrome(s: str) -> bool:
    pass
# Schreibe eine rekursive Funktion count_consonants(s), die die Anzahl der Konsonanten in einer Zeichenkette s zählt.


def count_cons(s :str) -> int:
    if len(s) < 1:
        return 0
    elif s[0] in 'aeiou':
        return 1 + count_cons(s[1:])
    else:
        return 0 + count_cons(s[1:])

print(count_cons("anaeiouna"))