import math

def fact(n):
    prod = n
    for m in range(n-1, 1, -1):
        prod *= m
    return prod

def comb(n,r):
    return math.factorial(n) / (math.factorial(r) * (math.factorial(n-r)))

def P85(n, err):
    x = 3
    solutions = {}
    loop = True
    while loop:
        for y in range(2, x):
            r = comb(x,2)*comb(y,2)
            if n-err < r < n+err:
                solutions[abs(r)] = (r, x-1,y-1)
            if r > 1000000000:
                loop = False
        x += 1
    return solutions[min(solutions.keys())]

print(P85(2000000, 10))