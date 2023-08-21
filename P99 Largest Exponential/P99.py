import math

def importFile(path):
    with open(path) as f:
        lines = f.readlines()
        data = [list(map(int,line.split()[0].split(","))) for line in lines]
    return data

def f(e1,e2):
    if e1[1]*math.log(e1[0]) > e2[1]*math.log(e2[0]):
        return e1
    else:
        return e2

def P99():
    b_e_pairs = importFile("p099_base_exp.txt")
    
    largest_i = 0
    for pair in b_e_pairs:
        if f(pair, b_e_pairs[largest_i]) == pair:
            largest_i = b_e_pairs.index(pair)
    return largest_i

print(P99())