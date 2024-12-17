# test_unittest.py
import unittest
from zadanie_skoczki_ale_klasowo import Szachownica  # Import klasy Szachownica z pliku main.py

class TestSzachownica(unittest.TestCase):
    def test_brak_szachowania(self):
        dane = [(0, 0), (2, 2)]
        szachownica = Szachownica(rozmiar=8, skoczkowie=dane)
        wynik = szachownica.znajdz_szachujace_sie_skoczki()
        self.assertEqual(wynik, [])

    def test_dwa_szachujace_sie_skoczki(self):
        dane = [(0, 0), (2, 1)]
        szachownica = Szachownica(rozmiar=8, skoczkowie=dane)
        wynik = szachownica.znajdz_szachujace_sie_skoczki()
        self.assertEqual(wynik, [((0, 0), (2, 1))])

    def test_wiecej_niz_dwa_szachujace_sie(self):
        #print(self)
        dane = [(0, 0), (2, 1), (4, 2)]
        szachownica = Szachownica(rozmiar=8, skoczkowie=dane)
        wynik = szachownica.znajdz_szachujace_sie_skoczki()
        self.assertEqual(wynik, [((0, 0), (2, 1)), ((2, 1), (4, 2))])

unittest.main()
