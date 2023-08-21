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

def primeFactors(number, prime_map, prime_list):
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
    return factorised_form

prime_map = createPrimes(1000000)
primes = [p for p in range(0, len(prime_map)) if prime_map[p] != 0]