import timeit
import math

# x is same input as math.factorial() input
def trailingZeroes(x):
    zero_count = 0
    p = 5
    while x/p > 1:
        zero_count += math.floor(x/p)
        p *= 5
    return zero_count

def factorial(x):
    f = x
    for i in range(2, x):
        f *= i
    return f

#print(math.factorial(1000000000000))
#print(trailingZeroes(1000000000000))
print(factorial(1000000000000))