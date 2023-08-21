from math import sqrt, tan, atan
import random

def m(x1,y1,x2,y2): # general gradient formula
    return (y1-y2)/(x1-x2)

def m_o(x,y): # line tangent to point on ellipse
    return -((4*x)/y)

def get_c(m, a, b): # y-intersect
    return m*-a+b

def m_r(m_n, m_i): # When m_n OR m_i is negative and the other positive
    return tan(atan(m_n) + abs(atan(m_n)-atan(m_i)))

def get_y(m, x, c): # returns correct y based of off x, m, c, this is because there are two POSSIBLE y coordinates (+/-sqrt(...))
    return m*x + c

def ellipseIntersect(m, c): # returns the x coordinates of BOTH intersection points of line and ellipse
    print([(-m*c + 2*sqrt(25*m**2 - c**2 + 100))/(4 + m**2),
            (-m*c - 2*sqrt(25*m**2 - c**2 + 100))/(4 + m**2)])
    return [(-m*c + 2*sqrt(25*m**2 - c**2 + 100))/(4 + m**2),
            (-m*c - 2*sqrt(25*m**2 - c**2 + 100))/(4 + m**2)]

#x1, y1... = first line (the original incident ray on entry)
def P144(x1, y1, x2, y2):
    # line is stored as array; y=mx+c -> [m, c, a, b]
    # where a, b are the newest set of coordinates, i.e. last intersection
    lines = []
    
    p_line = [m(x1,y1,x2,y2), get_c(m(x1,y1,x2,y2), x2, y2), x2, y2]
    #print(m(x1,y1,x2,y2))
    #n_line = [m_r(-1/m_o(p_line[2],p_line[3]), p_line[0])] # gradient
    #n_line.append(get_c(n_line[0],p_line[2],p_line[3])) # y-intersect
    #n_line.append(ellipseIntersect(n_line[0], n_line[1])[0]) # x-value of intersect
    #n_line.append(get_y(n_line[0], n_line[2], n_line[1])) # y-value of intersect
    #print(n_line)
    
    for i in range(0, 4):
        #print(p_line)
        n_line = [m_r(-1/m_o(p_line[2],p_line[3]), p_line[0])] # gradient
        n_line.append(get_c(n_line[0],p_line[2],p_line[3])) # y-intersect
        n_line.append(ellipseIntersect(n_line[0], n_line[1])[i%2]) # x-value of intersect
        n_line.append(get_y(n_line[0], n_line[2], n_line[1])) # y-value of intersect
        p_line = n_line
        #print(p_line)
        lines.append(n_line)
        n_line = []
    return lines

#P144(0,10,1.4,-9.6)
print(m_r(-1/m_o(0.387, -9.97), -329.5777908510203))
print(ellipseIntersect(-329.5777908510203, 117.72673351684254))