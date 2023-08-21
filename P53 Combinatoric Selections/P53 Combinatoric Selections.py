def factorial(n):
    prod = 1
    for x in range(2, n+1):
        prod *= x
    return prod

def combinations(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

def P53(lim1, par):
    count = 0
    for n in range(1, lim1+1):
        for r in range(1, n):
            if combinations(n,r) > par:
                count += 1
    return count

print(P53(400, 1000000))