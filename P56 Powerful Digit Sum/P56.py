def digitalSum(n):
    return sum(list(map(int, list(str(n)))))

def P56(a_lim, b_lim):
    max_digit_sum = 0
    for a in range(1, a_lim):
        for b in range(1, b_lim):
            n = a**b
            digital_sum = digitalSum(n)
            if digital_sum > max_digit_sum:
                max_digit_sum = digital_sum
    return max_digit_sum

print(P56(101,101))