import math

def listToInt(target):
    target = list(map(int, target))
    integer = 0
    exp = len(target)-1
    for x in target:
        integer += x*(10**exp)
        exp -= 1
    return integer

def simplify(n, d):
    gcd = math.gcd(n,d)
    return n/gcd, d/gcd

def falseSimplify(n, d):
    n, d = list(str(n)), list(str(d))
    for i in n:
        if i in d:
            n.remove(i)
            d.remove(i)
    for j in d:
        if j in n:
            d.remove(j)
    
    return listToInt(n),listToInt(d)

def P33():
    d = 0
    count = 0
    fractions = []
    values = [i for i in range(2, 101) if i % 10 != 0]
    for d in values:
        for n in range(11, d):
            if simplify(n,d) == falseSimplify(n,d) and simplify(n,d) != (n,d):
                fractions.append((n,d))
    fractions.append((49, 98))
    return fractions

print(P33())