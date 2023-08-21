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

def rad(n, prime_map = createPrimeMap(100000)):
    if prime_map[n] == 1:
        return n, n
    
    prod = 1
    for x in range(0, int(n/2)+1):
        if prime_map[x] == 1 and n % x == 0:
            prod *= x
    return n, prod

def P124():
    E = []
    prime_map = createPrimeMap(1000000)
    for i in range(1, 100001):
        E.append(rad(i, prime_map))
    return E

E = P124()
E.sort(key=lambda x:x[1])
print(E[9999][0])