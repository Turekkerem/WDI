class Skoczek:
    def __init__(self, wiersz, kolumna):
        """
        Reprezentacja pojedynczego skoczka na szachownicy.
        """
        self.wiersz = wiersz
        self.kolumna = kolumna

    def pozycja(self):
        """
        Zwraca aktualną pozycję skoczka w formie krotki (wiersz, kolumna).
        """
        return self.wiersz, self.kolumna

    def moze_szachowac(self, inny):
        """
        Sprawdza, czy ten skoczek może szachować innego skoczka.
        """
        ruchy = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        for rw, rk in ruchy:
            if self.wiersz + rw == inny.wiersz and self.kolumna + rk == inny.kolumna:
                return True
        return False


class Szachownica:
    def __init__(self, rozmiar, skoczkowie):
        """
        Inicjalizuje szachownicę o danym rozmiarze i listę skoczków.
        """
        self.rozmiar = rozmiar
        self.skoczkowie = [Skoczek(w, k) for w, k in skoczkowie]
        for pozycje in skoczkowie:
            if pozycje[0]>rozmiar or pozycje[1]>rozmiar:
                raise IndexError

    def znajdz_szachujace_sie_skoczki(self):
        """
        Zwraca listę par skoczków wzajemnie się szachujących.
        """
        szachujace = []
        liczba_skoczkow = len(self.skoczkowie)
        
        for i in range(liczba_skoczkow):
            for j in range(i + 1, liczba_skoczkow):  # Unikamy powtarzania par
                if self.skoczkowie[i].moze_szachowac(self.skoczkowie[j]):
                    szachujace.append((self.skoczkowie[i].pozycja(), self.skoczkowie[j].pozycja()))
        return szachujace

    def wizualizuj(self):
        """
        Wizualizuje szachownicę z pozycjami skoczków.
        """
        szachownica = [['.' for _ in range(self.rozmiar)] for _ in range(self.rozmiar)]
        for skoczek in self.skoczkowie:
            szachownica[skoczek.wiersz][skoczek.kolumna] = 'S'
        
        for wiersz in szachownica:
            print(' '.join(wiersz))

