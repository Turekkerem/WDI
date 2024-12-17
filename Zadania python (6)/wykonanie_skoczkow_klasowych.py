from zadanie_skoczki_ale_klasowo import Szachownica
dane = [(0, 0), (2, 1), (4, 2),(5,4),(7,7),(6,5)]
szachownica = Szachownica(rozmiar=8, skoczkowie=dane)

# Wizualizacja szachownicy
print("Szachownica:")
szachownica.wizualizuj()

# Znalezienie skoczków, które się szachują
szachujace = szachownica.znajdz_szachujace_sie_skoczki()
print("\nSkoczki szachujące się wzajemnie:", szachujace)