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

def P71(original, max_d):
    x = original[0]/original[1]
    smallest_diff = 1
    frac = (0,0)
    for d in range(9, max_d+1):
        n = int(original[0]*d/original[1])
        frac_dec = n/d
        diff = x - frac_dec
        if euclid(n,d)==1 and diff < smallest_diff:
            smallest_diff = diff
            frac = (n,d)
    return frac

print(P71((3,7), 1000000))