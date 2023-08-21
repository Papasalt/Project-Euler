def f(n):
    return 4*n**2-4*n+1
def g(n):
    return 4*n**2-10*n+7
def h(n):
    return 4*n**2-8*n+5
def d(n):
    return 4*n**2-6*n+3

def P28(dim):
    sum_of_diagonals = 1
    functions = [f,g,h,d]
    for func in functions:
        for x in range(2,(dim-int(0.5*dim-1.5))):
            sum_of_diagonals += func(x)
    return sum_of_diagonals

print(P28(1001))