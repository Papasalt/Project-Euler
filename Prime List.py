import timeit
import math

def primeList(upper_lim=1000):
    prime_numbers = list(range(3, upper_lim, 2))
    prime_numbers.insert(0, 2)
    i = 0
    while i < int(math.sqrt(len(prime_numbers))):
        #print(prime_numbers, "\n")
        current_prime = prime_numbers[i] # 2
        i2 = (i+1)**2
        while i2 < len(prime_numbers):
            if prime_numbers[i2] % current_prime == 0:
                del prime_numbers[i2]
            i2 += 1
        i += 1
    return prime_numbers

def primeList2(n=10**7):
    A = [1]*(n+1)
    i = 2
    while i < math.sqrt(n):
        if A[i] == 1:
            i2 = 0
            j = i
            while j**2 + (i2*j) <= n:
                A[j**2 + i2*j] = 0
                i2 += 1
        i += 1
    print(len(A))
    return A

# Python 3 program for
# implementation of
# Sieve of Atkin
 
def sieveOfAtkin(limit=1000):
 
    # Initialise the sieve
    # array with False values
    sieve = [False] * limit
    for i in range(0, limit):
        sieve[i] = False
 
    '''Mark sieve[n] is True if
    one of the following is True:
    a) n = (4*x*x)+(y*y) has odd
    number of solutions, i.e.,
    there exist odd number of
    distinct pairs (x, y) that
    satisfy the equation and
    n % 12 = 1 or n % 12 = 5.
    b) n = (3*x*x)+(y*y) has
    odd number of solutions
    and n % 12 = 7
    c) n = (3*x*x)-(y*y) has
    odd number of solutions,
    x > y and n % 12 = 11 '''
    x = 1
    while x * x < limit:
        y = 1
        while y * y < limit:
 
            # Main part of
            # Sieve of Atkin
            n = (4 * x * x) + (y * y)
            if (n <= limit and (n % 12 == 1 or
                                n % 12 == 5)):
                sieve[n] ^= True
 
            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True
 
            n = (3 * x * x) - (y * y)
            if (x > y and n <= limit and
                    n % 12 == 11):
                sieve[n] ^= True
            y += 1
        x += 1
 
    # Mark all multiples of
    # squares as non-prime
    r = 5
    while r * r < limit:
        if sieve[r]:
            for i in range(r * r, limit, r * r):
                sieve[i] = False
 
        r += 1
 
        # Print primes
    # using sieve[]
             
#print(sieveOfAtkin(10**6))
print(timeit.timeit(primeList2, number = 1))
print(timeit.timeit(sieveOfAtkin, number = 1))