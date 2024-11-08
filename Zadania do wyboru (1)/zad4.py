def f(x):
    return x*x-2
def miejsca_zerowe(p=-1000000,k=1000000,ile=0):
    if ile>1:#ile - zmienna która na podstawie obserwacji i heurystyki ma pokazać programowi kiedy już więcej rozwiązań nie znajdzie
        exit(0)
    s=(p+k)/2
    while 1:
        if ile>1:
            exit(0)
        s=(p+k)/2
        if -0.00000000000001<f(s)<0.00000000000001:
            print(s)
            miejsca_zerowe(s+0.5,1000000,ile+1)
        if f(p)*f(s)<0:
            k=s
        else:
            p=s
miejsca_zerowe()
