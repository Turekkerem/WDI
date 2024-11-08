"""p = open("pin.txt","r")
s = open("saldo.txt", "r")"""
def logowanie():
    print("Witamy! Wprowadz PIN aby kontynuowac")
    pin_wprowadzony=input()
    p = open("pin.txt","r")
    pin=p.read()
    while pin!=pin_wprowadzony:
        print("PIN niepoprawny")
        print("Sprobuj ponownie")
        pin_wprowadzony=input()
def pokaz_dostepne_operacje():
    print("1 - Wplacic pieniadze")
    print("2 - Wyplacic pieniadze")
    print("3 - sprawdzic saldo")
    print("Wprowadz cyfre dzialania aby kontynuowac")
def nastepna_akcja():
    print("Co chcialbys zrobic ?")
    print("1 - Skorzystac z bankomatu ponownie")
    print("2 - wyjsc z programu")
    p=int(input())
    if p==1:
        bankomat()
    elif p==2:
        print("Dziekujemy za skorzystanie z naszych uslug")
        exit(0)
    else:
        print("Wystapil blad - sprobuj ponownie")
        nastepna_akcja()
def bankomat():
    print("Witamy ponownie! Co chcialbys zrobic?")
    #pokaz_dostepne_operacje()
    #print("test")
    czy=0
    while czy==0:
        operacja=input()
        if operacja!='1' and operacja!='2' and operacja!="3":
            print("Wystapil blad, prosze o wpisanie ponownie")
            pokaz_dostepne_operacje()
        else:
            czy=1
    if operacja=='3':
        s = open("saldo.txt", "r")
        print(f"Twoj stan rachunku wynosi {s.read()}")
        s.close()
        nastepna_akcja()
    elif operacja=='1':
        s = open("saldo.txt","r")
        ile=int(input("Ile chcialbys wplacic?"))
        sal=int(s.read())+ile
        s = open("saldo.txt","w")
        s.write(str(sal))
        print(f"Wplaciles {ile} i aktualnie posiadasz {sal}")
        s.close()
        nastepna_akcja()
    else:
        s = open("saldo.txt","r")
        ile_na_koncie=int(s.read())
        ile=int(input("Ile chcialbys wyplacic?"))
        s.close()
        while ile>ile_na_koncie:
            print("Nie mozesz wyplacic wiecej niz masz na koncie - wybierz mniejsza kwote")
            ile=int(input("Ile chcialbys wyplacic?"))
        print(f"Wyplaciles {ile} zostalo Ci {ile_na_koncie-ile}")
        f = open("saldo.txt","w")
        f.write(str(ile_na_koncie-ile))
        f.close()
        nastepna_akcja()
logowanie()
pokaz_dostepne_operacje()
bankomat()
