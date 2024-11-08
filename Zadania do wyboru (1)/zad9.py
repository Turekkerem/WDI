def suma_dzielnikow(n):
    i=1
    s=0
    while i*i<n:
        if n%i==0:
            s+=i
            s+=n//i
        i+=1
    if i*i==n:
        s+=i
    return s-n
def czy_istnieje_zaprzyjazniona(a):
    sa=suma_dzielnikow(a)
    b=sa
    sb=suma_dzielnikow(sa)
    if b==sa and sb==a:
        return a,b
    return 0,0
for i in range(1000000):
    a,b=czy_istnieje_zaprzyjazniona(i)
    if a>0:
        print(a,b)
    
    