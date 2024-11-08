def czy_doskonala(n):
    i=1
    s=0
    while i*i<n:
        if n%i==0:
            s+=i
            s+=n//i
        i+=1
    if i*i==n:
        s+=i
    return s==2*n
for i in range(1,1000000):
    if czy_doskonala(i):
        print(i)