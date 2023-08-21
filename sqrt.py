import math
import timeit

squares = [x**2 for x in range(1,100000)]
def sqrt(x=1234):
    a = 1
    for i in range(0,10):
        a = (a**2 + x)/(2*a)
    return a

def sqrt2(x=1234):
    return math.sqrt(x)

print(timeit.timeit(sqrt,number=1000000))
print(timeit.timeit(sqrt2,number=1000000))