import math
from decimal import *
getcontext().prec = 1000

def CF_period(n):
    x = [Decimal(n).sqrt()]
    a = [x[-1].quantize(Decimal("1"), rounding=ROUND_DOWN)]
    period = 0
    while True:
        period += 1
        x.append(1/(x[-1]-a[-1]))
        a.append(x[-1].quantize(Decimal("1"), rounding=ROUND_DOWN))
        if a[-1] == 2*a[0]:
            return period

count = 0
for i in [x for x in list(range(1, 10001)) if not math.sqrt(x).is_integer()]:
    print(i)
    if CF_period(i) % 2 != 0:
        count += 1

print(count)