def fibo(n):
    a=1
    b=1
    s=100
    while a*b<n:
        s=a+b
        a=b
        b=s
        if a*b==n:
            print("TAK",a,b)
            exit(0)
    print("NIE")
    exit(0)
fibo(int(input()))