#from symengine import *
import sympy

def p(n):
    series = " + ".join([f"x**{i}" for i in range(0, n+2, 1)])
    for j in range(2, n+2):
        print(j)
        s = " + ".join([f"x**{i}" for i in range(1, n+2, j)])
        series = f"({series})*({s})"
        series = sympy.expand(sympy.sympify(series))
    return sympy.Poly(series).all_coeffs()

print(p(10))