import math
import collections
import timeit

def isPrime(number=65463):
    for x in range(2, math.ceil(math.sqrt(number))+1):
        if number % x == 0:
            return False
    return True

def getNextPrime(start):
    if start == 2:
        return 3
    x = start + 2
    while True:
        if isPrime(x) == True:
            return x
        x += 2

def createPrimeList(minimum, maximum):
    primes = [x for x in range(minimum, maximum)]
    #print(primes)
    for x in range(2, math.ceil(math.sqrt(maximum))):
        for p in primes:
            if p % x == 0 and p != x:
                primes.remove(p)
    return primes

prime_list = createPrimeList(2, math.ceil(math.sqrt(342476400)))
def numberOfDivisors(number=342476400):
    factorised_form = collections.defaultdict(int)
    calc = number
    i = 0
    while isPrime(calc) == False:
        current_prime = prime_list[i]
        temp = calc/current_prime
        if temp.is_integer() == True:
            calc = temp
            factorised_form[current_prime] += 1
        else:
            i += 1
    factorised_form[calc] += 1
    #print(factorised_form.items())
    n_of_divisors = 1
    for exp in factorised_form.values():
        n_of_divisors *= (exp+1)
    #p_e = list(map(lambda x:x+1, factorised_form.values()))
    #n_of_divisors = np.prod(p_e) #p_e = array of prime factors' exponents + 1
    return n_of_divisors

def slowNumberOfDivisors(number=342476400):
    counter = 2
    for x in range(2, math.ceil(math.sqrt(number))):
        if number % x == 0:
            counter += 1
    return counter

print("Fast numberOfDivisors: ", timeit.timeit(numberOfDivisors, number = 1)) # You have to change arguments in function manually
print("Slow numberOfDivisors: ", timeit.timeit(slowNumberOfDivisors, number = 1))
#print(numberOfDivisors(1000))