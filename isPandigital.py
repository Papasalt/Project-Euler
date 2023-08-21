def isPandigital(n):
    digits = [0,0,0,0,0,0,0,0,0]
    for d in str(n):
        digits[int(d)-1] += 1
    return all([i==1 for i in digits])

print(isPandigital(1234567891))