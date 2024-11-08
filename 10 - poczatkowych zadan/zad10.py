import random
def wb(a):
    if a>=0:
        return a
    return -a
def pot(a,b):
    if b==0:
        return 1
    if b%2==0:
        t=pot(a,b//2)
        return t*t
    return a*pot(a,b-1)
def pier(p):
    a=1
    b=p/a
    while wb(a-b)>0.0000001:
        a=(a+b)/2
        b=p/a
    return (a+b)/2
def kalkulator():
    while True:
        # Pobranie dwóch liczb od użytkownika
        a = float(input("Wprowadź pierwszą liczbę: "))
        b = float(input("Wprowadź drugą liczbę: "))

        # Pobranie operacji od użytkownika
        operacja = input("Wybierz operację (+, -, *, /, ^, #, x): ")

        # Wykonanie odpowiedniej operacji
        if operacja == '+':
            print(f"Wynik dodawania: {a + b}")
        elif operacja == '-':
            print(f"Wynik odejmowania: {a - b}")
        elif operacja == '*':
            print(f"Wynik mnożenia: {a*b}")
        elif operacja == '/':
            if b != 0:
                print(f"Wynik dzielenia: {a / b}")
            else:
                print("Błąd: nie można dzielić przez zero.")
        elif operacja == '^':
            print(f"Wynik potęgowania: {pot(a,b)}")
        elif operacja == '#':
            if a >= 0:
                print(f"Pierwiastek kwadratowy z {a}: {pier(a)}")
            else:
                print("Błąd: nie można pierwiastkować liczby ujemnej.")
        elif operacja == 'x':
            random.randint(a, b)
            print(f"Wylosowana liczba z zakresu {a} - {b}: {random.randint(a, b)}")
        else:
            print("Niepoprawny symbol operacji.")

        # Zapytanie o kontynuację
        kontynuacja = input("Czy chcesz wprowadzić nowe dane? (T/N): ").upper()
        if kontynuacja != 'T':
            print("Kalkulator został zakończony.")
            break

# Uruchomienie kalkulatora
kalkulator()
