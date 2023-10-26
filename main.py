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
    x = x // 16

    return wygladwhexadecymalnym

x = int(input("Podaj Dodatnia Cyfre: "))
ostWynik = konwersjanaszesnasatkowy(x)
print("wyglad w systemie szesnastkowym: ", ostWynik)




