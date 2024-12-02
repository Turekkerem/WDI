from random import randint
def pokaz(plansza):
    for i in range(len(plansza[0])):
        for j in range(len(plansza[0])):
            print(plansza[i][j],end=' ')
        print()
def wstaw_gonce(plansza,dane):
    for x,y in dane:
        plansza[x-1][y-1]='G'
    return plansza
def dodawanie_wartosc_do_slownika(slownik,klucz,wartosc):
    if klucz not in slownik:
        slownik[klucz]=wartosc
    return slownik
def czy_atakuje_z_mojego_pola(w,k,plansza,ktore=0):
    #print("start",w,k)
    licznik=0 #liczba do 4
    global dane
    wp=w-1#wspolrzedne poprawne
    kp=k-1
    wsp_kon=len(plansza[0])
    czy=0
    wpk=wp#kopie poprawne
    kpk=kp
    wspolrzedne=[]
    while wpk<wsp_kon-1 and kpk<wsp_kon-1:#powiekszam obie
        wpk+=1
        kpk+=1
        #print("test",wpk,kpk)
        if plansza[wpk][kpk]=='G':
            # and (wpk,kpk) not in dane:
            licznik+=1
            #print(w,k,wpk,kpk)
            wspolrzedne.append((wpk+1,kpk+1))
            break
    wpk=wp#kopie poprawne
    kpk=kp
    while wpk>0 and kpk>0:#pomniejszam obie
        wpk-=1
        kpk-=1
        if plansza[wpk][kpk]=='G':
# and (wpk,kpk) not in dane:
            licznik+=1
            #print(w,k,wpk,kpk)
            wspolrzedne.append((wpk+1,kpk+1))
            break
            
    wpk=wp#kopie poprawne
    kpk=kp
    while wpk<wsp_kon-1 and kpk>0:#powiekszam wiersz a kolumne pomniejszam
        wpk+=1
        kpk-=1
        if plansza[wpk][kpk]=='G':# and (wpk,kpk) not in dane:
            
            licznik+=1
            #print(w,k,wpk,kpk)
            wspolrzedne.append((wpk+1,kpk+1))
            break
    wpk=wp#kopie poprawne
    kpk=kp
    while wpk>0 and kpk<wsp_kon-1:#pomniejszam wiersz a powiekszam kolumne
        wpk-=1
        kpk+=1
        if plansza[wpk][kpk]=='G':# and (wpk,kpk) not in dane:
            
            licznik+=1
            #print(w,k,wpk,kpk)
            wspolrzedne.append((wpk+1,kpk+1))
            break
    #print(w,k,wspolrzedne)
    return licznik,(wspolrzedne)
def jakie_gonce_sie_szachuja(plansza,dane):
    ile_jest_atakow=0
    ws=[]
    co_atakuje_co=[]
    co_atakuje_co_dict=dict()
    a=0#zmienna pocomnicza
    for k in range(len(dane)):
        a,ws=czy_atakuje_z_mojego_pola(dane[k][0],dane[k][1],plansza,k)
        co_atakuje_co.append([dane[k][0],dane[k][1],ws])
        co_atakuje_co_dict=dodawanie_wartosc_do_slownika(co_atakuje_co_dict,(dane[k][0],dane[k][1]),ws)
        #print(co_atakuje_co[-1])
        ile_jest_atakow+=a
    """
    for i in range(len(co_atakuje_co)):
        if len(co_atakuje_co[i][2])>0:
            print(co_atakuje_co[i][0],co_atakuje_co[i][1]," atakuje: ",end=' ')
            print()
            for j in co_atakuje_co[i][2]:
                print("\t",j)
            print()
    """
    #print(co_atakuje_co)
    #print(ile_jest_atakow)
    #print("nowe")
    print('='*40)
    print('Wypisanie w czytelnej formie jaki goniec \"do czego ma dostęp\"')
    for key in co_atakuje_co_dict:
        if co_atakuje_co_dict[key]!=[]:
            print(key,co_atakuje_co_dict[key])
    print('='*40)
    return co_atakuje_co_dict
def wypisanie_parami(dic):
    pary=[]
    for i in dic:
        a=i
        blista=dic[i]
        for b in blista:
            if (a,b) not in pary or (b,a) not in pary:
                pary.append((a,b))
    for i in pary:
        print(i)
    t=len(pary)//2
    print(f"Występuje ogólnie {t} różnych ataków")
    return  t#zwrac ilosc atakow
def random_goniec_time(plansza,ilosc=9999):
    dane_nowe=[]
    while ilosc>0:
        a=randint(1,len(plansza[0])-1)
        b=randint(1,len(plansza[0])-1)      
        
        ilosc-=1
    return dane_nowe
ilosc_atakow=0 #ile atakow goncow wystepuje (dwa wzajemnie atakujace sie gonce sa jednym atakiem)
wielkosc=100
plansza=[['N' for _ in range(wielkosc)] for _ in range(wielkosc)]
#dane=[(1,3),(3,3),(6,7),(2,4),(7,1),(6,1)]
#dane=[(3,3),(7,7),(77,77),(99,99),(76,78)]
#dane=[(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7)]
dane=random_goniec_time(plansza)
plansza=wstaw_gonce(plansza,dane)
#pokaz(plansza)
dic=jakie_gonce_sie_szachuja(plansza,dane)
ile_atakow=wypisanie_parami(dic)