import math

def nextRotation(x):
    x = str(x)
    n = ""
    for i in range(0, len(x)):
        n += x[i-1]
    return int(n)

def createPrimes(lim):
    prime_map = [0,0] + [1 for i in range(2, lim)] #len(prime_map) == len(numbers) when returning
    i = 1
    while i != lim:
        if prime_map[i] != 0:
            for j in range(2*i, lim, i):
                prime_map[j] = 0
            i += 1
        else:
            i += 1
    return prime_map

def isCircularPrime(n, prime_map):
    rotation = nextRotation(n)
    for _ in range(0, len(str(n))):
        if prime_map[rotation] == 0:
            return False
        rotation = nextRotation(rotation)
    return True

def P35(lim):
    prime_map = createPrimes(lim)
    primes = [p for p in range(0, len(prime_map)) if prime_map[p] != 0]
    count = 0
    for x in primes:
        if isCircularPrime(x, prime_map):
            count += 1
    return count

print(P35(1000000))