import math
import itertools

def listToInt(target):
    target = list(map(int, target))
    integer = 0
    exp = len(target)-1
    for x in target:
        integer += x*(10**exp)
        exp -= 1
    return integer

def isPandigital(n):
    n = str(n)
    digits = [0,0,0,0,0,0,0,0,0]
    for d in n:
        digits[int(d)-1] += 1
    return all([i==1 for i in digits[:len(n)]])

def isPrime(number):
    for x in range(2, math.ceil(math.sqrt(number))+1):
        if number % x == 0:
            return False
    return True

def P41():
    largest_prime = 0
    count = 0
    for i in itertools.permutations([1,2,3,4,5,6,7]):
        x = listToInt(i)
        if x > largest_prime and isPrime(x) == True:
            largest_prime = x
    return largest_prime

print(P41())