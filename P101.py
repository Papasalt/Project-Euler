from decimal import Decimal

# ex. pol = [[6,-11,6],[2,1,0]]
def evalPol(pol,n):
    x = 0
    for t in range(0,len(pol[0])):
        x += pol[0][t]*n**pol[1][t]
    return x

def generatorFunction(pol,start,end):
    for x in range(start,end):
        n = 0
        for t in range(0,len(pol[0])):
            n += pol[0][t]*x**pol[1][t]
        yield n

# ex. p = [[x1,x2,x3...],[y1,y2,y3...]]
def lagrangeInterp(p, n):
    x = 0
    for j in range(0,len(p[0])):
        a = 1
        for i in range(0,len(p[0])):
            if i != j:
                a *= Decimal((n - p[0][i])) / Decimal((p[0][j] - p[0][i]))
        x += a*p[1][j]
    return x

points = [[1,2,3,4],[1,8,27,64]]
#print(evalPol([[6,-11,6],[2,1,0]], 4))
#print(lagrangeInterp(points,5))

def P101(pol):
    s_FIT = 0
    points = [[1],[1]]
    n = 2
    while lagrangeInterp(points,n+1) != evalPol(pol, n+1):
        if lagrangeInterp(points,n+1) != evalPol(pol, n+1):
            l = lagrangeInterp(points,n)
            s_FIT += int(l)
            if l < 0:
                print(l, points)
                break
        if n > 90:
            break
        #print(points)
        points[0].append(n)
        points[1].append(evalPol(pol,n))
        n += 1
    return s_FIT

gen = [[1,-1,1,-1,1,-1,1,-1,1,-1,1],[0,1,2,3,4,5,6,7,8,9,10]]
print(P101(gen))
#print(lagrangeInterp([[1,2],[1,8]],2))