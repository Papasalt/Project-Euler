import time

def fib(n):
    a = 0
    b = 1
    c = None
    for i in range(1,n):
        c = b
        b += a
        a = c
        yield b,i

def isPandigital(n):
    digits = [0,0,0,0,0,0,0,0,0]
    for d in str(n):
        digits[int(d)-1] += 1
    return all([i==1 for i in digits])


start = time.time()
for f in fib(1000000):
    if isPandigital(str(f[0])[:9]) and isPandigital(str(f[0])[-9:]):
        print(f)
        break
print(time.time()-start)