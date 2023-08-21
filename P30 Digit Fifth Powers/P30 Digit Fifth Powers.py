import math

def sumDigitPowers(digits, power):
    val = 0
    for d in digits:
        val += d**power
    return val

def P30(number, power):
    digits = []
    for i in range(math.floor(math.log10(number)), -1, -1):
        digits.append(int(number / int(math.pow(10, i)) % 10))
    if sumDigitPowers(digits, power) == number:
        return True
    return False

nums = []
for i in range(1000, 1000000):
    if P30(i, 5) == True:
        nums.append(i)
print(sum(nums))