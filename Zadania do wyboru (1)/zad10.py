def nwd(a,b):
    while b>0:
        c=a%b
        a=b
        b=c
    return a
a = int(input())
b = int(input())
c = int(input())
print(nwd(a,nwd(b,c)))