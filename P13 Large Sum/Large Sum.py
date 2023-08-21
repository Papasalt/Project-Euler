import numpy as np
import itertools

path = "100 50-Digit Numbers.txt"

def importNumbersAsStr(path):
    numbers = []
    with open(path, "r") as file:
        lines = file.readlines()
        for line in lines:
            numbers.append(line.rstrip().split(" "))
    return numbers

def convertAllToInt(input_list):
    for line_i in range(len(input_list)):
        input_list[line_i] = list(map(int, input_list[line_i]))
    return input_list

numbers = list(itertools.chain.from_iterable(convertAllToInt(importNumbersAsStr(path))))
print(sum(numbers))