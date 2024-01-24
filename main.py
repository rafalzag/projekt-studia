# różne numery rzędów w samolocie Embraer 170 PLL LOT podczas wyboru miejsca pasażerów
arr = [4, 8, 1, 9, 12, 3, 17, 2, 10, 5, 6, 25, 20, 21, 15, 7, 23, 16, 24, 11, 18, 19, 13, 14, 22]
print("Przed sortowaniem:", arr)

swapped = True

# musimy jakoś je posortować na potrzeby późniejszego loadsheetu i określenia środka ciężkości
while swapped:
    swapped = False
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True

print("Po sortowaniu:", arr)

# z racji, że dla każdego rzędu są 4 miejsca oznaczone literami od A do D, to chciałbym je dodać

sorted_arr_with_letters = [f"{value}{letter}" for value in arr for letter in "ABCD"]

print("Po sortowaniu z literą miejsca:", sorted_arr_with_letters)

# no to mamy już miejsca do loadsheetu do wyważenia samolotu, teraz losowo umieszczamy pasażerów na wybranych miejscach

import random # tu wrzucam random, aby za każdym razem dawało nam inne wyniki

sorted_arr_with_info = []

for value in arr:
    for letter in "ABCD":
        weight = random.randint(40, 120)
        sorted_arr_with_info.append(f"{value}{letter} - {weight} kg")

print("Po dodaniu wag każdego pasażera:", sorted_arr_with_info)

# zsumujmy wagę pasażerów z każdego rzędu

row_weights = {}

for item in sorted_arr_with_info:
    seat_label, weight_str = item.split('-')

    # Pobierz tylko cyfry z numeru rzędu
    row_number = ''.join(char for char in seat_label if char.isdigit())

    # Obsługa różnych form zapisu wagi
    weight_str = weight_str.split()[0].strip()  # Get the first part before any space and remove leading/trailing spaces
    weight = int(weight_str)

    if row_number not in row_weights:
        row_weights[row_number] = 0

    row_weights[row_number] += weight

print("Suma wag dla każdego rzędu:", row_weights)

# przyjmując, że środek ciężkości jest na wyskości 13 rzędu, to sprawdź czy cięższe są przednie rzędy czy tylne rzędy

# Funkcja do obliczania różnicy w masie między przednimi a tylnymi rzędami
def roznica_wagi_przed_tyl(arrangement):
    wagi_przednich_rzedow = sum(row_weights[str(i)] for i in arrangement[:srodek_ciezkosci])
    wagi_tylnych_rzedow = sum(row_weights[str(i)] for i in arrangement[srodek_ciezkosci:])
    return wagi_przednich_rzedow - wagi_tylnych_rzedow

# Środek ciężkości na wysokości 13 rzędu
srodek_ciezkosci = 13

# Suma wag przednich rzędów
wagi_przednich_rzedow = sum(row_weights[str(i)] for i in range(1, srodek_ciezkosci))

# Suma wag tylnych rzędów
wagi_tylnych_rzedow = sum(row_weights[str(i)] for i in range(srodek_ciezkosci + 1, max(map(int, row_weights.keys())) + 1))

# Różnica w wadze między przednimi a tylnymi rzędami
roznica_wagi = abs(wagi_przednich_rzedow - wagi_tylnych_rzedow)

# Informacja o przesunięciu środka ciężkości
if wagi_przednich_rzedow > wagi_tylnych_rzedow:
    print(f"Środek ciężkości jest przesunięty do tyłu, o {roznica_wagi} kg.")
elif wagi_przednich_rzedow < wagi_tylnych_rzedow:
    print(f"Środek ciężkości jest przesunięty do przodu, o {roznica_wagi} kg.")
else:
    print("Środek ciężkości jest w odpowiednim miejscu.")

# zakładając, że środek ciężkości jest przesunięty za bardzo do przodu (rzędy 1-12) lub do tyłu (rzędy 14-25) zwróć komunikat: uwaga samolot niewyważony!

# Przesunięcie maksymalne dozwolonego środka ciężkości (ustawiłem 100 kg tak randomowo)
maks_przesuniecie = 100  # To warto dostosować do rzeczywistych parametrów samolotu

# Informacja o przesunięciu środka ciężkości
if roznica_wagi > maks_przesuniecie:
    print(f"Uwaga! Samolot niewyważony. Przesunięcie środka ciężkości wynosi {roznica_wagi} kg, co przekracza maksymalne dozwolone przesunięcie.")
elif wagi_przednich_rzedow > wagi_tylnych_rzedow:
    print(f"Środek ciężkości jest przesunięty do tyłu, o {roznica_wagi} kg.")
elif wagi_przednich_rzedow < wagi_tylnych_rzedow:
    print(f"Środek ciężkości jest przesunięty do przodu, o {roznica_wagi} kg.")
else:
    print("Środek ciężkości jest w odpowiednim miejscu.")








