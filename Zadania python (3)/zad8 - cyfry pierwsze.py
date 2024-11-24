def wczytaj():
    try:
        n=int(input("Podaj n : "))
    except ValueError:
        print("Podaj liczbę naturalną n={1,2,3,......}")
        return wczytaj()
    tab=[[0]*n]*n
    for i in range(n):
        print(f"Wczytaj {i+1}. rząd")
        pokaz(tab,n)
        for j in range(n):
            tab[i][j]=int(input(f"      Wprowadź {j+1}. liczbę z {i+1} rzędu: "))
    return tab,n
def wczytaj_2():
    try:
        n=int(input("Podaj n : "))
    except ValueError:
        print("Podaj liczbę naturalną n={1,2,3,......}")
        return wczytaj_2()
    tab=[]
    for i in range(n):
        print(f"Wczytaj {i+1}. rząd")
        #pokaz(tab,n)
        row=list(map(int,input().split()))
        if len(row)!=n:
            print("Niestety nie udalo sie sprobuj jeszcze raz")
            return wczytaj_2()
        tab.append(row)
    return tab,n
def czy_z_cyfr_pierwszych(liczba):
    while liczba>0:
        if liczba%10 not in [2,3,5,7]:
            return 0
        liczba//=10
    return 1
def czy_spelnia(tab,n):
    #s=[[0]*n]*n
    suma=0
    for i in range(n):
        for j in range(n):
            #print("suma",suma)
            #s[i][j]=czy_z_cyfr_pierwszych(tab[i][j])
            if czy_z_cyfr_pierwszych(tab[i][j]):
                #print("kolejny")
                suma+=1
                break
    return suma==n
def pokaz(tab,n):
    print("="*n*2)
    for i in range(n):
        for j in range(n):
            print(tab[i][j],end=' ')
        print()
    print("="*n*2)
def generuj_z_liczba(ile,liczba):
    tab=[]
    for i in range(ile):
        row=[]
        for j in range(ile):
            row.append(liczba)
        tab.append(row)
    print(tab)
    return tab
t,n=wczytaj_2()
pokaz(t,n)
print(czy_spelnia(t,n))
tab=[[1,1,1],[4,4,4],[45,45,45]]
#tab=[[23,332,57],[75,23,55],[77,33333333332,73]]
#tab=generuj_z_liczba(10,37)
pokaz(tab,n)
print(czy_spelnia(tab,3))
    

