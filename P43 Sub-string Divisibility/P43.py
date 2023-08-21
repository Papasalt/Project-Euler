def createPrimes(lim):
    prime_map = [0,0] + [1 for i in range(2, lim)]
    i = 1
    while i != lim:
        if prime_map[i] != 0:
            for j in range(2*i, lim, i):
                prime_map[j] = 0
            i += 1
        else:
            i += 1
    return prime_map

def listToInt(target):
    target = list(map(int, target))
    integer = 0
    exp = len(target)-1
    for x in target:
        integer += x*(10**exp)
        exp -= 1
    return integer

def swap(target, i1, i2):
    target[i1], target[i2] = target[i2], target[i1]
    return target

def permute(target):
    length = len(target)-1
    key = length
    while key > 0 and target[key] <= target[key-1]:
        key -= 1
    key -= 1
    if key < 0:
        return 0 #is in reverse sorted order; last permutation
    
    newKey = length
    while newKey > key and target[newKey] <= target[key]:
        newKey -= 1
    
    swap(target, key, newKey)
    key += 1
    while length > key:
        swap(target, length, key)
        key += 1
        length -= 1
    return 1

def subStringDivisibility(n, primes):
    n = str(n)[1:]
    for i in range(0,7):
        if int(n[i:i+3]) % primes[i]:
            return False
    return True

def P43():
    target = [0,1,2,3,4,5,6,7,8,9]
    prime_map = createPrimes(1000)
    primes = [i for i in range(0, len(prime_map)) if prime_map[i] == 1]
    total = 0
    for i in range(0, 3628800): #10!
        n = listToInt(target)
        if subStringDivisibility(n, primes) == True:
            total += n
        permute(target)
    return total

print(P43())