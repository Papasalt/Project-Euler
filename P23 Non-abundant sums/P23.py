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

def sumOfPDivisors(n, prime_map, primes):
    factorised_form = primeFactors(n, prime_map, primes)
    s_divisors = 1
    for p, e in factorised_form.items():
        a = 1
        for i in range(1, e+1):
            a += p**i
        s_divisors *= a
    return s_divisors-n

def abundantNums():
    nums = []
    prime_map = createPrimes(100000)
    primes = [p for p in range(0, len(prime_map)) if prime_map[p] != 0]
    for n in range(2, 28124):
        if sumOfPDivisors(n, prime_map, primes) > n:
            nums.append(n)
    return nums

def isSumOfN(n, A):
    for i in A:
        if n-i in A:
            return True
    return False

def P23():
    abundant_nums = set(abundantNums())
    s = 0
    for i in range(1, 28124):
        if not isSumOfN(i, abundant_nums):
            s += i
        print(i)
    return s

print(P23())