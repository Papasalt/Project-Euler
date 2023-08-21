import collections
import timeit

def p(n=200):
    # increased by one to increase all range functions, otherwise they would run i < n, rather than i <= n
    n += 1
    series = collections.defaultdict(int, {e:1 for e in range(0,n,1)}) # {exponent : coefficient}
    for j in range(2, n):
        current_series = list(series.items())[:n]
        for i in range(1,n//2+1):
            delta_e = i*j
            for term in current_series:
                series[term[0]+delta_e] += term[1]
    return series[n-1]

print(p(20))