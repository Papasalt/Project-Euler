import math
import timeit

def isPrime(n):
    if n % 2 == 0 and n != 2 or n == 1:
        return False
    for x in range(3, int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True
# Used to check if fraction results in a recurring decimal
def primeFactors(n):
    prime_factors = []
    for x in range(2, int(n/2)+1):
        if n % x == 0 and isPrime(x) == True:
            prime_factors.append(x)
    return prime_factors

# ! numerator must be coprime to denominator !
def periodLength(denominator): #type(fraction) == tuple where n1 is numerator and n2 is denominator
    k = 1
    prime_factors = primeFactors(denominator)
    if prime_factors == [2, 5] or prime_factors == [2] or prime_factors == [5]:
        return 0 # fraction does not result in recurring decimal
    while True:
        if denominator % 2 == 0:
            denominator /= 2
        elif denominator % 5 == 0:
            denominator /= 5
        else:
            break
    while True:
        #print(((10**1)-1) % int(denominator))
        if ((10**k)-1) % int(denominator) == 0:
            print(k)
            break
        k += 1
    return k

longest_period = 0
d = 0
#for x in range(3, 1000):
    #current_period_length = periodLength(x)
    #if current_period_length > longest_period:
        #longest_period = current_period_length
        #print(periodLength(x), "\t", x)
        #d = x

print(periodLength(7))