import math
import timeit

def isPrime(n):
    if n % 2 == 0 and n != 2:
        return False
    for x in range(3, int(math.sqrt(n)+1), 2):
        if n % x == 0:
            return False
    return True

def isPermutation(n1, n2):
    n1,n2 = str(n1),str(n2)
    digital_occurences_n1 = [0,0,0,0,0,0,0,0,0,0]
    digital_occurences_n2 = [0,0,0,0,0,0,0,0,0,0]
    for n in n1:
        digital_occurences_n1[int(n)] += 1
    for n in n2:
        digital_occurences_n2[int(n)] += 1
    if digital_occurences_n1 == digital_occurences_n2:
        return True
    return False

def primeList(s, e):
    primes = []
    for i in range(s, e):
        if isPrime(i):
            primes.append(i)
    return primes

def primePermutations(primes=primeList(1488, 10000)):
    d1 = 0
    d2 = 0
    for p1 in range(0, len(primes)):
        for p2 in range(p1+1, len(primes)):
            d1 = primes[p2]-primes[p1]
            for p3 in range(p2+1, len(primes)):
                d2 = primes[p3]-primes[p2]
                if d1 == d2 and isPermutation(primes[p1],primes[p2]) and isPermutation(primes[p2],primes[p3]):
                    return [primes[p1], primes[p2], primes[p3]]
print(timeit.timeit(primePermutations, number = 1))