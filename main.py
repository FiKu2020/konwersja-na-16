def konwersjanaszesnasatkowy(x):
    if x < 0:
        return "Podaj liczbę dodatnią"

    wygladwhexadecymalnym = ''

    while x > 0:
        resztaDzielenia = x % 16
        x = x // 16
        if resztaDzielenia < 10:
            wygladwhexadecymalnym = str(resztaDzielenia) + wygladwhexadecymalnym
        else:
            wygladwhexadecymalnym = chr(ord('A') + resztaDzielenia - 10) + wygladwhexadecymalnym

    return wygladwhexadecymalnym


x = int(input("Podaj liczbę dodatnią: "))
ostWynik = konwersjanaszesnasatkowy(x)
print("Wygląd w systemie szesnastkowym:", ostWynik)