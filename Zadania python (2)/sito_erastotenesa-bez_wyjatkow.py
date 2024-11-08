def meine_floor(n):#można skorzystac z blblioteki math i uzyc funkcji floor lub ceil ale to by wymagalo yzcia tej bliblioteki
    a = round(n,0)
    if n - a >= 0:
        return a
    return a-1
def czy_to_int(n):
    return meine_floor(n)==n
def sito(n=100):
    #n+=1
    ilorazy_i_reszty=[]
    if n<=2:
        #return [],[]
        print([])
        print([])
        return
    p=[1]*(n+2)
    p[0]=0
    p[1]=0
    i=2
    while i*i<=n:
        if p[i]==1:
            for j in range(2*i,n+1,i):
                p[j]=0
        i+=1
    pierwsze=[2]#aby wygodniej sie liczyło ilorazy i reszty
    
    k=1#licznik liczacy ilosc liczb pierwszych
    for i in range(3,n):
        if p[i]==1:
            pierwsze.append(i)
            #//iloraz_calkowity=pierwsze[k]//pierwsze[k-1]
            ilorazy_i_reszty.append([pierwsze[k]//pierwsze[k-1],pierwsze[k]%pierwsze[k-1]])
            k+=1
    print(pierwsze)
    print(ilorazy_i_reszty)
    #return pierwsze,ilorazy_i_reszty
def licz(w_czym_licz,co_licz):#zwraca ilosc podanych znaków w łańcuchu znakow ; można użyć .count()
    l=0
    for i in w_czym_licz:
        l+=(co_licz==i)
    return l
def czy_zawiera_cos_innego_niz_cyfry(nstr):
    p=ord('0')
    #print(nstr)
    nstr=nstr.strip()
    #nstr=nstr.strip('-')
    l1=licz(nstr,'.')
    l2=licz(nstr,',')
    if not ((l1*l2==0) and (l1+l2<=1)):
        return 1
    for i in nstr:
        if p<=ord(i)<=p+9 or i=='.' or i==',' or i=='-': # or nstr==' ' or nstr=="   ":
            continue
        else:
            return 1
    return 0
def wczytywanie_liczby():#wczytująca i zwracająca wartość wczytaną przez uzytkownika wtedy i tylko wtedy gdy watość jest liczbą naturalną (dla zera zwraca pustą listę)
    print("Wczytaj liczbę naturalną:")
    n_str=input()
    if czy_zawiera_cos_innego_niz_cyfry(n_str):
        print("Wprowadzona wartość zawiera znaki inne niż cyfry (oraz przecinek lub kropkę) - spróbuj ponownie")
        return wczytywanie_liczby()
    n=float(n_str)
    if n<0:
        print("Wprowadzona liczba jest ujemna - spróbuj ponownie")
        return wczytywanie_liczby()
    if czy_to_int(n)==0:#cG9zaWFkYV93YWR5X3ByemV6X3B5dGhvbm93eV9mbG9hdA==
        print("Wprowadzona wartość wartość jest ułamkowa - spróbuj ponownie")
        return wczytywanie_liczby()
    return int(n)
        
    
sito(wczytywanie_liczby())
