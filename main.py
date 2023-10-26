def konwersjanaszesnasatkowy(x):
    if x < 0:
        return ("podaj dodatnia")
    wygladwHexadecymalnym = ''

    while x > 0:
        resztaDzielenia = x % 16
    if resztaDzielenia > 10:
        wygladwhexadecymalnym = resztaDzielenia + wygladwhexadecymalnym;
    else:
        wygladwhexadecymalnym = chr(ord('A') + resztaDzielenia - 10) + wygladwhexadecymalnym
    return wygladwhexadecymalnym




x = int(input("Podaj dodatnia cyfre: "))
print(wygladwhexadecymalnym)






