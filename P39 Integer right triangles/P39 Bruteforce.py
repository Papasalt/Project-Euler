import math
import collections

triangles = [] #[s1,s2,hyp]
count = collections.defaultdict(int) # {perimeter : count}
l = 1000
for x in range(1, l+1):
    for y in range(x, l+1):
        triangles.append((x,y, math.sqrt(x**2+y**2)))
        hyp = math.sqrt(x**2+y**2)
        if sum([x,y,hyp]).is_integer() and sum([x,y,hyp]) < l+1:
            count[sum([x,y,hyp])] += 1
print(max(count, key=count.get))