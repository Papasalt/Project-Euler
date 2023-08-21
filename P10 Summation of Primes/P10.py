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

prime_map = createPrimes(21)
primes = [p for p in range(0, len(prime_map)) if prime_map[p] != 0]
print(sum(primes))