def wb(a):#funkcja obliczajaca wartosc bezwzgledna liczby podanej jako argument funkcji
    if a>=0:
        return a
    return -a
def pier(p):
    a=1
    b=p/a
    """Petla typu while ponizej dziala na zasadzie robienia sredniej z obu liczb 
    mogących być graficzną interpretacja bokow
    kwadratu na początku zdefiniowane(przed tym komentarzem) zmienna a i b ktorych iloczyn
      caly czas będzie równy polu czyli liczby ktora chcemy spierwiastkowacc"""
    while wb(a-b)>0.0000001:
        a=(a+b)/2
        b=p/a
    return (a+b)/2
a = float(input("Prosze o podanie pierwszej liczby: "))
b = float(input("Prosze o podanie drugiej liczby: "))
if a<0 and b<0:
    print("Obie liczby sa ujemne - wyjscie z programu")
    exit(0)
a=wb(a)
b=wb(b)
print(f"Suma podanych liczb wynosi {a+b}")
print(f"Roznica podanych liczb wynosi {a-b}")
il=a*b
if il==10:
    print(f"Iloczyn podanych liczb wynosi {a*b} Yay!")
else:
    print(f"Iloczyn podanych liczb wynosi {a*b}")
print(f"Iloraz podanych liczb wynosi {a/b}")
print(f"Kwadrat pierwszej liczby to: {a*a}")
print(f"Kwadrat drugiej liczby to: {b*b}")
print(f"Pierwiastek kwadratowy pierwszej liczby to: {pier(a)}")
print(f"Pierwiastek kwadratowy drugiej liczby to: {pier(b)}")