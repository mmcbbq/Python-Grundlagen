liste = [40, 8, 63, 60, 12, 4, 13, 82, 87, 87, 87, 84, 85, 39, 57, 55, 72, 6, 46, 18, 5, 97, 78, 64, 94, 64, 62, 22, 11,
         89, 92, 53, 22, 51, 44, 49, 6, 87, 57, 20, 39, 67, 87, 49, 71, 79, 80, 94, 19, 57, 13, 71, 51, 99, 68, 31, 80,
         63, 41, 17, 25, 7, 88, 86, 29, 58, 99, 63, 28, 59, 2, 34, 15, 73, 36, 90, 9, 75, 61, 40, 1, 23, 71, 94, 75, 46,
         59, 72, 73, 63, 93, 90, 68, 7, 29, 92, 44, 74, 84, 80]
suche = 83
liste = (sorted(liste))
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = 0
r = len(liste) - 1

mitte = (l + r) // 2
print(f' \n l: {l} \n r:{r} \n mitte:{mitte}')
while True:
    print(f"pruefe {liste[mitte]}: index: {mitte}")
    if liste[mitte] == suche:
        print(f'gefunden index {mitte}')
        break
    elif liste[mitte] > suche:
        print("suche ist kleiner")
        r = mitte - 1
    elif liste[mitte] < suche:
        print('suche ist groesser')
        l = mitte + 1
    mitte = (l + r) // 2

    print('-----------------------------------------')
    print('-----------------------------------------')
    print('-----------------------------------------')
    print(f' \n l: {l} \n r:{r} \n mitte:{mitte}')
    if l > r:
        print('kein treffer')
        break
print(f"suche {suche}")
print(liste)




