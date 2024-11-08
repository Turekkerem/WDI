def wczytaj():
    try:
        n=int(input("Podaj n : "))
    except ValueError:
        print("Podaj liczbę naturalną n={1,2,3,......}")
        return wczytaj()
    tab=[[0]*n]*n
    for i in range(n):
        print(f"Wczytaj {i+1}. rząd")
        for j in range(n):
            tab[i][j]=int(input(f"      Wprowadź {j+1}. liczbę z {i+1} rzędu: "))
    return tab,n
def czy_z_cyfr_pierwszych(liczba):
    while liczba>0:
        if liczba%10 not in [2,3,5,7]:
            return 0
        liczba//=10
    return 1
def czy_spelnia(tab,n):
    s=[[0]*n]*n
    suma=0
    for i in range(n):
        for j in range(n):
            s[i][j]=czy_z_cyfr_pierwszych(tab[i][j])
            if czy_z_cyfr_pierwszych(tab[i][j]):
                suma+=1
                break
    return suma==n
t,n=wczytaj()
print(czy_spelnia(t,n))
    

