def isPalindrome(x):
    if str(x)[::-1]==str(x):
        return True
    return False

def reverseAdd(x):
    return x+int(str(x)[::-1])

def isLychrel(x, lim=50):
    for i in range(0,lim):
        x = reverseAdd(x)
        if isPalindrome(x):
            return False
    else:
        return True

def P55(m):
    count = 0
    for x in range(0,m):
        if isLychrel(x):
            count += 1
    return count

print(P55(10000))
