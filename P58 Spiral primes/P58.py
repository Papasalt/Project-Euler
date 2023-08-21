import math

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for d in range(3, math.ceil(math.sqrt(n)), 2):
        if n % d == 0:
            return False
    return True

def g(n):
    return 4*n**2-10*n+7
def h(n):
    return 4*n**2-8*n+5
def d(n):
    return 4*n**2-6*n+3

def P58():
    r = [3,5]
    i = 2
    while not r[0]/r[1] < 0.10:
        i += 1
        r[0] += sum([isPrime(g(i)), isPrime(h(i)), isPrime(d(i))])
        r[1] += 4
    return 2*i - 1

print(P58())