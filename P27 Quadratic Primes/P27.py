def createPrimeMap(lim):
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

def P27(a_lim, b_lim):
    prime_map = createPrimeMap(1000000)
    primes = [i for i in range(0, b_lim) if prime_map[i]]
    
    ans = 0
    largest_count = 0
    for b in primes:
        for a in range(-a_lim, a_lim):
            count = 0
            n = 0
            while True:
                if prime_map[n**2 + a*n + b] == 1 and n**2 + a*n + b > 0:
                    count += 1
                    n += 1
                else:
                    break
            if count > largest_count:
                largest_count = count
                ans = a * b
    return ans, largest_count

print(P27(1000, 1000))