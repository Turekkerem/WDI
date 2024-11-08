def konwerter1(n,a):
    liczba_w_dziesietnym=''

    for i in range(len(n)-1,-1,-1):
        nr_znaku=ord(n[i])
        if ord('0')<=nr_znaku<=ord('9'):
            liczba_w_dziesietnym+=(nr_znaku-ord('0'))*(a**(i+1))#można zastąpic funkcją szybkiego potęgowania
    return liczba_w_dziesietnym
def konwerter_z_10_na_cokolwiek(dec,b):
    if dec==0:
        return '0'
    w=''
    while dec>0:
        reszta=dec%b
        if reszta>=10:
            w=chr(reszta+ord('A')-10)+w
        else:
            w=str(reszta)+w
        dec//=10
    return w
def k1_k2(n,a,b):
    return konwerter_z_10_na_cokolwiek(konwerter1(n,a),b)
while 1:
    dec=int(input())
    n=int(input())
    print(konwerter_z_10_na_cokolwiek(dec,n))
