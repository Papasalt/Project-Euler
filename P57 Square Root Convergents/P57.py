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

def P57(n):
    n_CF = continuedFraction(n)
    P = [1, n_CF[0]]
    Q = [0, 1]
    n = 0
    for i in range(0, 1001):
        P.append(n_CF[1:][i%(len(n_CF)-1)]*P[-1]+P[-2])
        Q.append(n_CF[1:][i%(len(n_CF)-1)]*Q[-1]+Q[-2])
        if len(str(P[-1])) > len(str(Q[-1])):
            n += 1
    return n

print(P57(2))