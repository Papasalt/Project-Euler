import math
from decimal import *
getcontext().prec = 1000

def e(iterations):
    e = 1
    for i in range(1, iterations):
        e += Decimal(1)/Decimal(factorial(i))
    return e

def factorial(n):
    prod = 1
    for x in range(2, n+1):
        prod *= x
    return prod

def continuedFraction(n):
    x = [Decimal(n)]
    a = [x[-1].quantize(Decimal("1"), rounding=ROUND_DOWN)]
    for i in range(0, 1000):
        x.append(1/(x[-1]-a[-1]))
        a.append(x[-1].quantize(Decimal("1"), rounding=ROUND_DOWN))
    return a

def minimalSolution1(D): #naive bruteforce method
    x = 1
    while True and x < 1000000:
        if math.sqrt(1+D*(x**2)).is_integer():
            return int(math.sqrt(1+D*(x**2)))
        x += 1
    return 0 #no solution found

def minimalSolution2(D):
    D_CF = continuedFraction(D)
    P = [1, D_CF[0]]
    Q = [0, 1]
    i = 0 # simple counter used for counting iterations
    while i < 99:
        P.append(D_CF[1:][i%(len(D_CF)-1)]*P[-1]+P[-2])
        #Q.append(D_CF[1:][i%(len(D_CF)-1)]*Q[-1]+Q[-2]) #not required
        i += 1 # counter
    return P
convergent = minimalSolution2(e(1000))[-1]
print(sum(list(map(float, list(str(convergent))))))