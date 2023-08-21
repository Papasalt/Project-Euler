def createPrimeMap(lim):
    prime_map = [0,0] + [1 for i in range(2, lim)]
    i = 1
    while i != lim:
        if prime_map[i] != 0:
            for j in range(i**2, lim, i):
                prime_map[j] = 0
            i += 1
        else:
            i += 1
    return prime_map

def primeFactors(n, primes):
    factors = []
    i = 0
    p = primes[i]
    while p < n/2:
        p = primes[i]
        if n % p == 0:
            factors.append(p)
        i += 1
    return factors

def phi(n, primes):
    phi_n = n
    for p in primeFactors(n, primes):
        phi_n *= 1 - (1/p)
    return phi_n-1 #subtracted to account for problem in question

def P72(d):
    prime_map = createPrimeMap(1000000)
    primes = [p for p in range(0, 1000000) if prime_map[p] == 1]
    total = 0
    for i in range(1, d):
        total += phi(i, primes)
    return total

print(P72(1000000))