def gradient(coord1,coord2): #a is tuple as so: (x,y)
    return (coord1[1]-coord2[1])/(coord1[0]-coord2[0])

def y_intercept(m,a,b): #m = gradient
    return -m*a+b

def pos_neg(lst):
    neg_count, pos_count, zero_count = 0, 0, 0
    for x in lst:
        if x < 0:
            neg_count += 1
        elif x > 0:
            pos_count += 1
        else:
            zero_count += 1
    return pos_count, neg_count, zero_count

def importTrianglesFromTxt(path):
    triangle_list = []
    with open(path, "r") as txt:
        content = txt.read().replace("\n",",")
        triangle_list = content.split(",")
        del triangle_list[-1]
        triangle_list = list(map(int, triangle_list))
    return triangle_list

def originInTriangle(p1,p2,p3):
    y_intercepts = []
    y_intercepts.append(y_intercept(gradient(p1,p2),p1[0],p1[1]))
    y_intercepts.append(y_intercept(gradient(p2,p3),p2[0],p2[1]))
    y_intercepts.append(y_intercept(gradient(p3,p1),p3[0],p3[1]))
    #print(y_intercepts)
    pos_neg_count = pos_neg(y_intercepts)
    if pos_neg_count[0] == 2 and pos_neg_count[1] == 1:
        return True
    else:
        return False

a = (-547,712)
b = (-352,579)
c = (951,-786)

triangles = importTrianglesFromTxt("p102_triangles.txt")
g = gradient((835,-947),(-340,495))
print(g)
print(y_intercept(g,835,-947))