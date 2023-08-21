import timeit
"""
m = gradient
c = y-intersect
x2 = x coordinate of point not on initial line defined by m, c
y2 = y coordinate of point not on initial line defined by m, c
"""
def gradient(x1,y1,x2,y2):
    try:
        return (y1-y2)/(x1-x2)
    except ZeroDivisionError:
        return 1000

def regionDefiner(m, c, p):
    if m * p[0] + c > p[1]:
        return 0 # <
    else:
        return 1 # >

"""
vertices = [(x,y),(x,y),(x,y)]; each point of triangle
point = (x,y); point that is being checked to be inside the triangle
"""
def isInTriangle(point,vertices):
    for vertex_i in range(-1, len(vertices)-1):
        m = gradient(vertices[vertex_i][0],vertices[vertex_i][1],
                     vertices[vertex_i+1][0],vertices[vertex_i+1][1])
        c = m * -vertices[vertex_i][0] + vertices[vertex_i][1]
        if regionDefiner(m, c, vertices[vertex_i-1]) == 0:
            if point[1] > m * point[0] + c:
                return False
        else:
            if point[1] < m * point[0] + c:
                return False
    return True

def run():
    with open("p102_triangles.txt") as triangles_txt:
        triangles = []
        for triangle in triangles_txt:
            triangles.append(list(map(int, triangle.rstrip("\n").split(","))))
    
    triangles_containing = 0
    for triangle in triangles:
        if isInTriangle((0,0), [(triangle[0],triangle[1]),(triangle[2],triangle[3]),(triangle[4],triangle[5])]):
            triangles_containing += 1
print(timeit.timeit(run, number = 1))