def euclid(x,y):
    r = -1
    m = 0
    n = 0
    while r != 0:
        m = x//y
        r = x-(y*m)
        x = y
        n = y
        y = r
    return n

fractions = []
for d in range(2, 12001):
    fractions.append((1,d))
    for i in range(2, d):
        if euclid(i,d) == 1:
            fractions.append((i,d))

fractions = sorted(fractions, key=lambda frac: frac[0]/frac[1])
print(fractions.index((1,2))-fractions.index(1,3))