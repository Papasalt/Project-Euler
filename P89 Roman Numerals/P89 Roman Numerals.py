import timeit

numerals_const = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"
                    ,4:"IV",9:"IX",40:"XL",90:"XC",400:"CD",900:"CM"}

inverted_numerals_const = {v: k for k, v in numerals_const.items()}

subtracted_numerals = ["IV","IX","XL","XC","CD","CM"]

single_use = [5,50,500,5,50,500]

def maxBelow(n,numerals):
    if n >= 1000:
        return 1000
    x = 0
    sorted_numeral_key = list(sorted(numerals.keys())) 
    while sorted_numeral_key[x] <= n:
        x += 1
    return sorted_numeral_key[x-1]

def toNumeral(n):
    numerals=dict(numerals_const)
    numeral=[]
    while n > 0:
        x = maxBelow(n,numerals)
        if x in single_use:
            n -= x
            numeral.append(numerals.pop(x))
        else:
            n -= x
            numeral.append(numerals[x])
    return numeral

def toArabic(n):
    x = 0
    while len(n) != 0:
        if n[:2] in subtracted_numerals:
            x += inverted_numerals_const[n[:2]]
            n = n[2:]
        else:
            x += inverted_numerals_const[n[0]]
            n = n[1:]
    return x

def P89():
    roman_numerals_path = r"C:\Users\papas\Desktop\Python Scripts\Project Euler\P89 Roman Numerals\0089_roman.txt"
    with open(roman_numerals_path, "r") as roman_numerals_raw:
        roman_numerals = roman_numerals_raw.read().splitlines()
    
    characters_saved = 0
    for numeral in roman_numerals:
        n = toArabic(numeral)
        characters_saved += len(numeral)-len("".join(toNumeral(n)))
    
    return characters_saved

print(str(timeit.timeit(P89, number=1))+"s")
print(P89())