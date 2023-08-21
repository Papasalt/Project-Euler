def isPalindrome(num):
    if str(num)[::-1] == str(num):
        #print(num)
        return True
    else:
        return False

def P55():
    n_of_lychrel_nums = 0
    for i in range(1, 10000):
        num = i
        iterations = 0
        while True:
            num += int(str(num)[::-1])
            iterations += 1
            if isPalindrome(num):
                break
            if iterations >= 50:
                n_of_lychrel_nums += 1
                break
    return n_of_lychrel_nums

print(P55())