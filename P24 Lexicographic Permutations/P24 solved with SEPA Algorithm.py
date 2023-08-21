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

target = [0,1,2,3,4,5,6,7,8,9]
for i in range(0, 999999):
    permute(target)
print(target)