def isPandigital(n):
    digits = [0,0,0,0,0,0,0,0,0]
    for d in str(n):
        digits[int(d)-1] += 1
    return all([i==1 for i in digits])

def P38():
    largest = 0
    for n in range(2, 1000000):
        concat = ""
        i = 1
        while len(concat) < 9 and i < n:
            concat += str(n*i)
            if n == 192:
                print(concat)
            if int(concat) > largest and isPandigital(concat):
                largest = int(concat)
            i += 1
    return largest

print(P38())