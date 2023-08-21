import collections

def createPrimes(lim):
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

def numberOfDivisors(number, prime_map, prime_list):
    factorised_form = collections.defaultdict(int)
    calc = number
    i = 0
    while prime_map[int(calc)] == 0:
        current_prime = prime_list[i]
        temp = calc/current_prime
        if temp.is_integer() == True:
            calc = temp
            factorised_form[current_prime] += 1
        else:
            i += 1
    factorised_form[calc] += 1
    n_of_divisors = 1
    for exp in factorised_form.values():
        n_of_divisors *= (exp+1)
    return n_of_divisors

def P179():
    prime_map = createPrimes(10000001)
    primes = [i for i in range(0,len(prime_map)) if prime_map[i] == 1]
    
    c = 0
    for n in range(2,10**7 - 1):
        if numberOfDivisors(n,prime_map,primes) == numberOfDivisors(n+1,prime_map,primes):
            c += 1
    
    return c

print(P179())