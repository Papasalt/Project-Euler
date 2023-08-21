import collections
import timeit

def P78():
    n = 2000
    c = 1
    series = collections.defaultdict(int, {e:1 for e in range(0,n,1)}) # {exponent : coefficient}
    for j in range(2, n):
        print(j)
        current_series = list(series.items())[:n]
        for i in range(1,n//2+1):
            delta_e = i*j
            for term in current_series:
                series[term[0]+delta_e] += term[1]
        if series[c] % 1000000 == 0:
            return series[c]
        c += 1
    return -1

print(P78())