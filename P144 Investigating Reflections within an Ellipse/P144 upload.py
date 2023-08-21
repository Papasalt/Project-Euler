from math import sqrt, tan, atan

def t(x, y):
    return (-4*x)/y

def pX(m, c):
    intersect = [(-c * m + 2 * sqrt(-c * c + 25 * m*m + 100)) / (m*m + 4),
                 (-c * m - 2 * sqrt(-c * c + 25 * m*m + 100)) / (m*m + 4)]
    return intersect

def m(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)

class Line:
    def __init__(self, m=0, c=0, a=0, b=0):
        self.m = m
        self.c = c
        self.a = a
        self.b = b

def nextLine(l):
    line = Line()
    line.a = pX(l.m, l.c)[0] if round(pX(l.m, l.c)[0], 5) != round(l.a, 5) else pX(l.m, l.c)[1]
    line.b = l.m * (line.a - l.a) + l.b
    line.m = tan(2*atan(t(line.a, line.b)) - atan(l.m))
    line.c = line.m * -line.a + line.b
    return line

def P144():
    lines = [Line(m(0,10.1,1.4,-9.6), 10.1, 0, 10.1)]
    lines.append(nextLine(lines[-1]))
    i = 0
    while True:
        lines.append(nextLine(lines[-1]))
        i += 1
        if lines[-1].a > -0.01 and lines[-1].a < 0.01 and lines[-1].b > 0:
            break
    return i

print(P144())