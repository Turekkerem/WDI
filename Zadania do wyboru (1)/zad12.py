def fibo():
    a=1
    b=1
    s=100
    i=0
    print(a)
    while abs(b/a-s/b)>=0.0001 and i<400:
        #print(b)
        if i<30:
            print(b/a)
        i+=1
        s=a+b
        a=b
        b=s
    print("Ostatnie: ",b/a)
        
fibo()