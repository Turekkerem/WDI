def is_prime(n):
    if n==2:
        return 1
    if n%2==0:
        return 0
    i=3
    while i*i<=n:
        if n%i==0:
            return 0
        i+=2
    return 1
print(is_prime(int(input())))