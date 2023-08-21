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

def factors(n, prime_map):
    factor_set = set()
    max_f = int(n/2)+1
    for p in range(1, max_f):
        if prime_map[p] and n % p == 0:
            factor_set.add(p)
    return factor_set

def phi(n, prime_map):
    if prime_map[n] == 1:
        return n-1
    factor_set = factors(n, prime_map)
    phi_of_n = n
    for f in factor_set:
        phi_of_n *= 1 - (1/f)
    return int(phi_of_n)

prime_map = createPrimes(10000000)