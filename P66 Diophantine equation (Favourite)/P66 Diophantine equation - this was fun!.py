import math
from decimal import *
getcontext().prec = 1000

def continuedFraction(n):
    x = [Decimal(n).sqrt()]
    a = [x[-1].quantize(Decimal("1"), rounding=ROUND_DOWN)]
    while True:
        x.append(1/(x[-1]-a[-1]))
        a.append(x[-1].quantize(Decimal("1"), rounding=ROUND_DOWN))
        if a[-1] == 2*a[0]:
            break
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
    while P[-1]**2 - D * Q[-1]**2 != 1:
        P.append(D_CF[1:][i%(len(D_CF)-1)]*P[-1]+P[-2])
        Q.append(D_CF[1:][i%(len(D_CF)-1)]*Q[-1]+Q[-2])
        #print(f"{P[-1]}² - {D} × {Q[-1]}²")
        i += 1 # counter
    return P[-1], Q[-1]

largest_D = -1
largest_x = -1

for i in [x for x in list(range(1, 1001)) if not math.sqrt(x).is_integer()]:
    if minimalSolution2(i)[0] > largest_x:
        largest_D = i
        largest_x = minimalSolution2(i)[0]

print(minimalSolution2(661))