def loadPrimes(start=None, end=None):
    with open(r"C:\Users\papas\Desktop\Python Scripts\Project Euler\10000000 Prime Numbers.txt") as f:
        primes = list(map(int, f.read().splitlines()))
    return primes[start:end]

def loadPrimeMap(start=None, end=None):
    with open(r"C:\Users\papas\Desktop\Python Scripts\Project Euler\10000000 Prime Map.txt") as f:
        primes = list(map(int, f.read().splitlines()))
    return primes[start:end]

def numberOfDivisors(number, prime_map, prime_list):
    factorised_form = []
    calc = number
    i = 0
    while prime_map[int(calc)] == 0:
        current_prime = prime_list[i]
        temp = calc/current_prime
        if temp.is_integer() == True:
            calc = temp
            factorised_form.append(current_prime)
        else:
            i += 1
    factorised_form.append(int(calc))
    return factorised_form

def P187():
    prime_map = loadPrimeMap()
    primes = loadPrimes()
    
    c = 0
    for n in range(2,10**8):
        if len(numberOfDivisors(n, prime_map, primes)) == 2:
            print(n)
            c += 1
    return c

print(P187())