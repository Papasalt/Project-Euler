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

def P50(lim):
    prime_map = createPrimes(lim)
    primes = [p for p in range(0, len(prime_map)) if prime_map[p] != 0]
    consec_primes = []
    counts = []
    for i in range(0, len(primes)-1):
        count = 0
        p = i+2
        total = primes[i]+primes[i+1]
        while total < lim and p < len(primes):
            if prime_map[total] == 1:
                counts.append(count)
                consec_primes.append(total)
            count += 1
            total += primes[p]
            p += 1
    return consec_primes, counts

sol = P50(1000000)
print(sol[0][sol[1].index(max(sol[1]))])