def genTriplet(m,n,k=1):
    return (k*(m**2 - n**2), k*(2*m*n), k*(m**2 + n**2))

def solve(L):
    m = 2
    while True:
        l = False
        for n in range(1, m):
            for k in range(1, L//sum(genTriplet(m,n))+1):
                triplet = genTriplet(m,n,k)
                l = True
                if sum(triplet) == L:
                    return triplet
        m += 1
        if l == False:
            return -1

def solve2(L):
    solutions = []
    c = 0
    m = 2
    while True:
        for n in range(1,m):
            triplet = genTriplet(m,n)
            triplet_sum = sum(triplet)
            if triplet_sum > L:
                return solutions
                #return c
            if L % triplet_sum == 0:
                solutions.append(L/triplet_sum)
                c += 1
        m += 1

print(solve2(1200))