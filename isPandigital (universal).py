def isPandigital(n):
    n = str(n)
    digits = [0,0,0,0,0,0,0,0,0]
    for d in n:
        digits[int(d)-1] += 1
    return all([i==1 for i in digits])