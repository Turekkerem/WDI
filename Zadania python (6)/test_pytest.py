
import pytest
from zadanie_skoczki_ale_klasowo import Szachownica

def test_szachowanie_puste_dane():
    dane = []
    szachownica = Szachownica(rozmiar=8, skoczkowie=dane)
    wynik = szachownica.znajdz_szachujace_sie_skoczki()
    assert wynik == []

def test_niezgodnosc_wyniku():
    dane = [(0, 0), (2, 2)]
    szachownica = Szachownica(rozmiar=8, skoczkowie=dane)
    wynik = szachownica.znajdz_szachujace_sie_skoczki()
    assert wynik != [((0, 0), (2, 2))]

def test_wyjatki_poza_szachownica():
    with pytest.raises(IndexError):
        Szachownica(rozmiar=8, skoczkowie=[(9, 9),(10,10)])
