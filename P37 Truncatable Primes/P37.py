import math

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

def isValid(p, prime_map):
    for i in range(0,len(str(p))):
        if (prime_map[int(str(p)[i:])] == 0 or 
            prime_map[int(str(p)[:i+1])] == 0):
            return False
    return True

def P37():
    prime_map = createPrimes(1000000)
    primes = [i for i in range(0, 1000000) if prime_map[i]]
    ans = 0
    for p in primes[4:]:
        if isValid(p, prime_map) == True:
            print(p)
            ans += p
    return ans

print(P37())