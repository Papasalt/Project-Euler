"""
includes 0 for convenience due to 0-indexing.
0 should NOT be checked for primality as prime numbers
may only be integers greater than 0
"""
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

print(createPrimes(1500000).count(1))