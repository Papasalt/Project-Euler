import collections
import math

# General niche math functions

def loadPrimes(start=None, end=None):
    with open(r"C:\Users\papas\Desktop\Python Scripts\Project Euler\10000000 Prime Numbers.txt") as f:
        primes = list(map(int, f.read().splitlines()))
    return primes[start:end]

def loadPrimeMap(start=None, end=None):
    with open(r"C:\Users\papas\Desktop\Python Scripts\Project Euler\10000000 Prime Map.txt") as f:
        primes = list(map(int, f.read().splitlines()))
    return primes[start:end]

def euclidAlgorithm(x,y):
    r = -1
    m = 0
    n = 0
    while r != 0:
        m = x//y
        r = x-(y*m)
        x = y
        n = y
        y = r
    return n

def gcd(*arr):
    arr = [*arr]
    while len(arr) != 2:
        arr = [euclidAlgorithm(arr[0], arr[1])] + arr[2:]
    return euclidAlgorithm(arr[0], arr[1])

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
    return factorised_form, n_of_divisors

def binom(n,k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))