import math
import numpy as np
import collections
import time
import timeit

#%%
def isPrime(number):
    for x in range(2, math.ceil(math.sqrt(number))+1):
        if number % x == 0:
            return False
    return True

def nextPrime(start):
    if start == 2:
        return 3
    x = start + 2
    while True:
        if isPrime(x) == True:
            return x
        x += 2

def isTriangular(number):
    #print(number)
    if ((np.sqrt(8 * number + 1) - 1) / 2).is_integer():
        return True
    return False

def nextTriangularNumber(current_number, index):
    return current_number+(index+1)

def createPrimeRange(lim=100000):
    numbers = range(2, lim)
    prime_list = [prime for prime in numbers if isPrime(prime)]
    prime_list.insert(0, 2)
    return prime_list

def nthTriangularNumber(index):
    return (index*index+index)/2

def numberOfDivisors(number, prime_list):
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
    print(factorised_form)
    return n_of_divisors

def highlyDivisibleTriangularNumber(n_divisors, prime_list):
    i = 1
    t_number = 1
    while True:
        if numberOfDivisors(t_number, prime_list) > n_divisors:
            break
        t_number = nextTriangularNumber(t_number, i)
        i += 1
    return t_number
#%%
#primes = createPrimeRange(1000000)
#print(numberOfDivisors(500500500, primes))
#t0 = time.perf_counter()
#print(highlyDivisibleTriangularNumber(500, primes))
#t1 = time.perf_counter()
#runtime = t1-t0
#print(f"The algorithm took: {runtime}s to run (excluding prime range creation)")
#print(numberOfDivisors(35734, primes))
print(timeit.timeit(createPrimeRange, number = 1))
"""
output = 76576500
SOLVED!
"""