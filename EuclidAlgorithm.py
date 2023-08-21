def euclidAlgorithm(x,y):
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

def gcd(*arr):
    arr = [*arr]
    while len(arr) != 2:
        arr = [euclidAlgorithm(arr[0], arr[1])] + arr[2:]
    return euclidAlgorithm(arr[0], arr[1])

print(gcd(456078, 3650748, 693045876))