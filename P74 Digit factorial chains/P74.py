from math import factorial

def chainGen(n):
    while True:
        n = sum([factorial(int(d)) for d in str(n)])
        yield n

def P74(lim, chain_length):
    total_count = 0
    for i in range(1, lim):
        sub_count = 0
        chain = set()
        for term in chainGen(i):
            pre_add = len(chain)
            chain.add(term)
            if len(chain) == pre_add:
                if len(chain) == chain_length-1:
                    total_count += 1
                    print(i)
                break
    return total_count

print(P74(1000000, 60))