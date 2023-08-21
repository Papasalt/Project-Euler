import math

def nLen(n):
    return math.floor(math.log10(n) + 1)

def P63():
    count = 0
    for x in range(1, 10):
        exp = 1
        while True:
            if nLen(x**exp) == exp:
                count += 1
                exp += 1
            else:
                break
    return count

print(P63())