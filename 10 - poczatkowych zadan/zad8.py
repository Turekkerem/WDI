def choinka_zwykla(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        print()
def choinka_bombki_i_szpic(n):
    for i in range(1, n + 1):
        czy=0
        for j in range(n - i):
            print(" ", end="")
        if i==1:
            print('X')
        else:
            for j in range(2 * i - 1):
                if (i//2==j and j%2==1) or (j%2==0 and i//2==j-i) and czy==0:
                    print('o',end="")
                    czy=1
                print("*", end="")
            print()
    for j in range(n-1):
            print(" ", end="")
    print("U")
n=int(input())
print("Przypadek A")
choinka_zwykla(n)
print("Przypadek D")
choinka_bombki_i_szpic(n)