import math

def nthPent(n):
    return n*(3*n-1)/2

def isPent(n):
    if ((-1-math.sqrt(1+24*n))/6).is_integer():
        return True
    else:
        return False

def valid(n1, n2): #n1 must be larger than n2
    if isPent(nthPent(n1)+nthPent(n2)) and isPent(nthPent(n1)-nthPent(n2)):
        return True
    return False

def P44():
    n1 = 1
    while True:
        for n2 in range(1, n1):
            if valid(n1,n2) == True:
                return nthPent(n1)-nthPent(n2)
        n1 += 1

print(P44())