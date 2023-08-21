import math
import time

def createPrimes(lim):
    prime_map = [0,0] + [1 for i in range(2, lim)]
    i = 1
    while i != lim:
        if prime_map[i] != 0:
            for j in range(2*i, lim, i):
                prime_map[j] = 0
            i += 1
        else:
            i += 1
    return prime_map

def binom(n,k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def P203(r):
    p_map  = createPrimes(20000000)
    primes = [i for i in range(0, len(p_map)) if 1 == p_map[i]]
    
    distinct_numbers = set()
    for n in range(0, r):
        for k in range(0, n+1):
            distinct_numbers.add(binom(n,k))
    
    squarefree_numbers = []
    for d in distinct_numbers:
        squarefree = True
        for p in primes:
            if d % p**2 == 0:
                squarefree = False
                break
            if p**2 > d:
                break
        if squarefree == True:
            squarefree_numbers.append(d)
    return sum(squarefree_numbers)

start = time.time()
print(P203(51))
print(f"Runtime: {time.time()-start}s")