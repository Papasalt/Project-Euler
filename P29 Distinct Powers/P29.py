def P29(a_lim, b_lim):
    values = []
    for a in range(2, a_lim+1):
        for b in range(2, b_lim+1):
            values.append(a**b)
    values = sorted(list(set(values)))
    return values

print(len(P29(100,100)))