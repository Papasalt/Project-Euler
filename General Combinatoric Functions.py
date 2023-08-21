def fact(n):
    prod = n
    for m in range(n-1, 1, -1):
        prod *= m
    return prod

def perm(n,r):
    p = n
    for m in range(n-1, n-r, -1):
        p *= m
    return p

def comb(n,r):
    return fact(n) / (fact(r) * (fact(n-r)))