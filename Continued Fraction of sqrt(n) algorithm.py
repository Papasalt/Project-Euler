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

def convergents(CF): #convergents given in fraction form
    Q = [0, 1]
    P = [1, CF[0]]
    i = 1
    for i in range(0, 200):
        P.append(CF[1:][i%(len(CF)-1)]*P[-1]+P[-2])
        Q.append(CF[1:][i%(len(CF)-1)]*Q[-1]+Q[-2])
        i += 1
    return Q, P

print(math.sqrt(13))
print(continuedFraction(13))
print(convergents(continuedFraction(661)))