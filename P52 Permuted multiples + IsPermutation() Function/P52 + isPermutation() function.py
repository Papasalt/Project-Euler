def isPermutation(*numbers):
    numbers = list(map(str, numbers))
    A = [] #originally named "digital_occurrences" but renamed due for list comprehension sakes
    for number in numbers:
        A.append([0,0,0,0,0,0,0,0,0,0])
        for n in number:
            A[-1][int(n)] += 1
    if all([A[a]==A[a+1] for a in range(0, len(A)-1)]):
        return True
    return False

def permutedMultiples():
    x = 1
    while True:
        if isPermutation(x,x*2,x*3,x*4,x*5,x*6):
            break
        x += 1
    return x

print(permutedMultiples())