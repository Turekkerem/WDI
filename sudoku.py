import random
import os

def generuj_plansze_sudoku():
    """
    Generuje podstawową planszę Sudoku z unikalnym rozwiązaniem za pomocą algorytmu backtrackingu.
    """
    plansza = [[0 for _ in range(9)] for _ in range(9)]
    wypelnij_przekatne_pudla(plansza)
    rozwiaz_plansze(plansza)
    return plansza

def wypelnij_przekatne_pudla(plansza):
    """
    Wypełnia przekątne 3x3 pudła planszy losowymi liczbami.
    """
    for i in range(0, 9, 3):
        wypelnij_pudlo(plansza, i, i)

def wypelnij_pudlo(plansza, wiersz, kolumna):
    """
    Wypełnia jedno pudło 3x3 na planszy losowymi liczbami.
    """
    liczby = list(range(1, 10))
    random.shuffle(liczby)
    for i in range(3):
        for j in range(3):
            plansza[wiersz + i][kolumna + j] = liczby.pop()

def czy_mozna_ustawic(plansza, wiersz, kolumna, liczba):
    """
    Sprawdza, czy można wstawić liczbę do danego pola planszy.
    """
    return (liczba not in plansza[wiersz] and
            liczba not in [plansza[i][kolumna] for i in range(9)] and
            liczba not in [plansza[wiersz//3*3 + i][kolumna//3*3 + j] for i in range(3) for j in range(3)])

def rozwiaz_plansze(plansza):
    """
    Rozwiązuje planszę Sudoku za pomocą algorytmu backtrackingu.
    """
    puste = znajdz_puste_pole(plansza)
    if not puste:
        return True
    wiersz, kolumna = puste
    for liczba in range(1, 10):
        if czy_mozna_ustawic(plansza, wiersz, kolumna, liczba):
            plansza[wiersz][kolumna] = liczba
            if rozwiaz_plansze(plansza):
                return True
            plansza[wiersz][kolumna] = 0
    return False

def znajdz_puste_pole(plansza):
    """
    Znajduje kolejne puste pole (oznaczone jako 0) na planszy.
    """
    for i in range(9):
        for j in range(9):
            if plansza[i][j] == 0:
                return i, j
    return None

def usun_pola_z_planszy(plansza, trudnosc=40):
    """
    Usuwa wybrane pola z planszy, tworząc łamigłówkę.
    """
    do_usuniecia = trudnosc
    while do_usuniecia > 0:
        wiersz = random.randint(0, 8)
        kolumna = random.randint(0, 8)
        if plansza[wiersz][kolumna] != 0:
            plansza[wiersz][kolumna] = 0
            do_usuniecia -= 1

def zapisz_plansze_do_pliku(plansza, nazwa_pliku):
    """
    Zapisuje planszę Sudoku do pliku w czytelnym formacie.
    """
    try:
        with open(nazwa_pliku, 'w') as f:
            for wiersz in plansza:
                f.write(" ".join(str(liczba) if liczba != 0 else "." for liczba in wiersz) + "\n")
    except IOError as e:
        print(f"Błąd zapisu do pliku {nazwa_pliku}: {e}")

def wyswietl_plansze(plansza):
    """
    Wyświetla planszę Sudoku w czytelnym formacie.
    """
    for wiersz in plansza:
        print(" ".join(str(liczba) if liczba != 0 else "." for liczba in wiersz))
    print()

def wyswietl_ozdobna_plansze(plansza):
    """
    Wyświetla planszę Sudoku w ozdobnym formacie z wyraźnymi podziałami na 3x3.
    """
    print("+" + "---+" * 6)
    for i, wiersz in enumerate(plansza):
        linia = "| " + " | ".join(
            " ".join(str(liczba) if liczba != 0 else "." for liczba in wiersz[j:j+3])
            for j in range(0, 9, 3)
        ) + " |"
        print(linia)
        if (i + 1) % 3 == 0:
            print("+" + "---+" * 6)

def generuj_i_zapisz_plansze(liczba, folder_wyjsciowy=None):
    """
    Generuje i zapisuje wskazaną liczbę plansz Sudoku do podanego folderu.
    Jeśli folder nie zostanie podany, używa domyślnego folderu programu.
    """
    if folder_wyjsciowy is None:
        # Ustaw domyślny folder na lokalizację programu
        folder_wyjsciowy = os.path.dirname(os.path.abspath(__file__))

    if not os.path.exists(folder_wyjsciowy):
        os.makedirs(folder_wyjsciowy)
    
    for i in range(1, liczba + 1):
        plansza = generuj_plansze_sudoku()
        usun_pola_z_planszy(plansza)
        print(f"Plansza Sudoku {i}:")
        wyswietl_ozdobna_plansze(plansza)
        nazwa_pliku = os.path.join(folder_wyjsciowy, f"plansza_sudoku_{i}.txt")
        zapisz_plansze_do_pliku(plansza, nazwa_pliku)


if __name__ == "__main__":
    try:
        liczba_plansz = int(input("Podaj liczbę plansz Sudoku do wygenerowania: "))
        folder_wyjsciowy = input("Podaj nazwę folderu do zapisania plansz (lub naciśnij Enter dla domyślnego): ").strip()
        folder_wyjsciowy = folder_wyjsciowy if folder_wyjsciowy else None
        generuj_i_zapisz_plansze(liczba_plansz, folder_wyjsciowy)
        print(f"Wygenerowano {liczba_plansz} plansz Sudoku i zapisano je w folderze: {folder_wyjsciowy or os.path.dirname(os.path.abspath(__file__))}.")
    except ValueError:
        print("Nieprawidłowa wartość. Wprowadź liczbę plansz jako liczbę całkowitą.")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")

