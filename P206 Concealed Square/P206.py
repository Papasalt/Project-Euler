import math

def match(n):
    n = str(n)
    j = 0
    for i in range(1, 10):
        if int(n[j]) != i:
            return False
        j += 2
    return True

def concealedSquare():
    n = 19293949596979899
    x = int(math.sqrt(n))+1
    while not match(x**2):
        x -= 2
    print(x*10)

concealedSquare()