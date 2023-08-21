def d(n): #function denoted as d as is in PE21
    val = 0
    for x in range(1, int(n/2)+2):
        if n % x == 0:
            val += x
    return val

def amicableNumbers(lim):
    val = 0
    for x in range(1, lim):
        a = d(x)
        b = d(a)
        if x == b and a != b:
            val += a + b
    return val/2

print(amicableNumbers(10000))