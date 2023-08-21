import math
from decimal import *
from itertools import filterfalse
getcontext().prec = 101

def isNotPerfectSquare(n):
    if math.sqrt(n).is_integer():
        return False
    return True

def P80_SQDE():
    total = 0
    for x in list(filter(isNotPerfectSquare, list(range(0, 100)))): #non-perfect squares
        val = list(str(Decimal(x).sqrt())[:-1])
        val.remove(".")
        total += sum(map(int, val))
    print(total)

P80_SQDE()