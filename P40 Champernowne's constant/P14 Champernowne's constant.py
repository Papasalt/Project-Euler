champernowne_c = "" #only includes numbers after the decimal point

for num in range(1, 1000000):
    champernowne_c += str(num)

val = 1
for x in range(0, 7):
    #print(val)
    val *= int(champernowne_c[10**x-1])

print(val)