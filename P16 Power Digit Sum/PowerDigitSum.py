def powerDigitSum(number, power):
    ans = 0
    for x in str(number**power):
        ans += int(x)
    return ans

for x in range(0, 100):
    print(powerDigitSum(2, x))