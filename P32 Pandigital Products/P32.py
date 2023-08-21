def isPandigital(*n):
    n = "".join(map(str, n))
    if "0" in n:
        return False
    digits = [0,0,0,0,0,0,0,0,0]
    for d in n:
        digits[int(d)-1] += 1
    return all([i==1 for i in digits])

def P32():
    pandigital_products = set()
    for x in range(1, 10000):
        for y in range(x, 10000):
            if isPandigital(x, y, x*y):
                pandigital_products.add(x*y)
    return sum(pandigital_products)

print(P32())