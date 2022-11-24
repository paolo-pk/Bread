# Gra, w której komputer odgaduje liczbę pomyślaną przez gracza

print("\nWitam w grze, w której komputer odganie liczbę, którą pomyślisz!")
print("ZACZYNAMY!!")
input("""
Pomyśl liczbę w przedziale od 1 do 100.
Za chwilę komputer zacznie odgadywanie Twojej liczby.
Jeśli będzie większa od Twojej, wpisz "za duża". Jeśli mniejsza, wpisz "za mała".
Jeśli komputer odgadnie Twoją liczbę, wpisz "brawo".
Gdy będziesz gotowa/y, wciśnij ENTER.""")

import random

liczba_losowa = random.randint(1, 100)
print("\nCzy to ta liczba: ", liczba_losowa)
odp_gracza = input("")
początek_przedziału = 1
koniec_przedziału = 100
while odp_gracza != "brawo":
    if odp_gracza == "za duża":
        koniec_przedziału = liczba_losowa
        liczba_losowa = random.randint(początek_przedziału + 1, liczba_losowa - 1)
        print("\nCzy to ta liczba: ", liczba_losowa)
        odp_gracza = input("")
    elif odp_gracza == "za mała":
        początek_przedziału = liczba_losowa
        liczba_losowa = random.randint(liczba_losowa + 1, koniec_przedziału - 1)
        print("\nCzy to ta liczba: ", liczba_losowa)
        odp_gracza = input("")
    else:
        print("\nCzy to ta liczba: ", liczba_losowa)
        odp_gracza = input("")
        
print("\nDZIĘKI ZA GRĘ! NIE BYŁO ŁATWO, ALE SIĘ UDAŁO!")
