def fibo():
    a=0
    b=1
    print(a)
    while b<1000000:
        print(b)
        s=a+b
        a=b
        b=s
fibo()