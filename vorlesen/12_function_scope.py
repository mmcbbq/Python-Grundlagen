# Eine Funktion, die eine lokale Variable definiert und nur innerhalb dieser Funktion verfügbar ist
def hallo():
    var = "local"  # 'var' ist lokal für hallo() und außerhalb dieser Funktion nicht verfügbar
    print(f'hallo: {var}')  # Gibt den Wert der lokalen Variable 'var' innerhalb von hallo() aus

hallo()  # Aufruf der Funktion gibt 'hallo: local' aus
# print(var)  # Fehler, weil 'var' außerhalb der Funktion hallo() nicht verfügbar ist

var = "global"  # 'var' wird hier als globale Variable definiert
hallo()  # Aufruf der Funktion hallo() überschreibt nicht die globale 'var' und gibt immer noch 'hallo: local' aus

print('###########################################################')
print('hallo_g')

# Funktion, die auf die globale Variable zugreift
def hallo_g():
    print(f'hallo_g: {var}')  # Zugriff auf die globale Variable 'var', da keine lokale 'var' in hallo_g() existiert

hallo_g()  # Gibt 'hallo_g: global' aus, da 'var' nun global als 'global' definiert wurde

print('###########################################################')
print('hallo_innen aussen')

# Eine Funktion, die auf eine nicht in der Funktion definierte Variable zugreifen will
def hallo_innen():
    print(f'hallo_innen: {var}')  # Zugriff auf die globale Variable 'var', wenn kein lokales 'var' in der Funktion hallo_innen() vorhanden ist

# Eine Funktion, die eine lokale Variable mit dem gleichen Namen wie die globale Variable verwendet
def hallo_aussen():
    var = "hallo_aussen"  # 'var' ist hier lokal und überschreibt die globale 'var' innerhalb von hallo_aussen()
    hallo_innen()  # Aufruf von hallo_innen() führt zu einem Fehler, wenn 'hallo_innen' versucht, auf das globale 'var' zuzugreifen
    print(f'hallo_aussen: {var}')  # Gibt den lokalen Wert von 'var' in hallo_aussen() aus

print('call hallo_aussen')
hallo_aussen()  # Hier wird hallo_innen() aufgerufen, aber es gibt einen Fehler, weil hallo_innen() die globale Variable erwartet

# Funktion, die mit dem 'global'-Keyword auf die globale Variable 'var' zugreift
def hallo_innen_global():
    global var  # 'var' wird hier als global deklariert, sodass hallo_innen_global() auf die globale 'var' zugreift und sie verändern kann
    print(f'hallo_innen: {var}')  # Gibt die globale Variable 'var' aus

# Funktion, die eine lokale Variable definiert und die globale Variable in hallo_innen_global() verwendet
def hallo_aussen():
    var = "hallo_aussen"  # Lokale Variable, die nur in hallo_aussen() verfügbar ist
    hallo_innen_global()  # Aufruf von hallo_innen_global(), das auf die globale Variable 'var' zugreift
    print(f'hallo_aussen: {var}')  # Gibt den lokalen Wert von 'var' in hallo_aussen() aus

print('call hallo_aussen innenglobal')
hallo_aussen()  # Aufruf von hallo_aussen() zeigt die lokale Variable 'var' in hallo_aussen() und die globale 'var' in hallo_innen_global()

print('global Keyword')

# Eine Funktion, die eine neue globale Variable erstellt
def erstelle_var(var2):
    global new_global  # Deklariert eine neue globale Variable 'new_global'
    new_global = var2  # Weist 'new_global' den Wert von 'var2' zu

erstelle_var(123)  # Erstellt die globale Variable 'new_global' und weist ihr den Wert 123 zu
print(new_global)  # Gibt den Wert von 'new_global' aus

print('-------------------Ändern der Übergabe----------------')

liste_ubergabe = ["alt", 2, 3, 4, 5]  # Globale Liste
var_ubergabe = "alt"  # Globaler String

# Funktion, die eine neue lokale Variable 'string' definiert
def change_string(string):
    string = "new"  # Lokale Änderung von 'string', hat keinen Effekt auf die globale 'var_ubergabe'

# Funktion, die eine Liste ändert (listen sind mutable)
def change_liste(liste):
    liste[0] = 'new'  # Ändert den ersten Wert der Liste, da listen mutable sind

change_string(var_ubergabe)
print(var_ubergabe)  # Gibt 'alt' aus, da var_ubergabe unverändert bleibt (strings sind immutable)
change_liste(liste_ubergabe)
print(liste_ubergabe)  # Gibt ['new', 2, 3, 4, 5] aus, da listen veränderlich (mutable) sind und die Änderung innerhalb der Funktion beibehalten wird























