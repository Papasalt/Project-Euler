import numpy as np
import timeit

def isTriangular(number):
    #print(number)
    if ((np.sqrt(8 * number + 1) - 1) / 2).is_integer():
        return True
    return False

def alphabeticalPositions(string): # assumes all values are upper-case
    return [x-64 for x in list(string.encode("ascii"))]

def codedTriangleNumbers(input_file_path=r"C:\Users\papas\Desktop\Python Scripts\Project Euler\P42 Coded Triangle Numbers\p042_words.txt"):
    # Parses the text file
    with open(input_file_path) as f:
        file_contents = f.read()
    file_contents = file_contents.replace("\"", "")
    words = file_contents.split(",")
    # Processes the text file contents and counts number of "triangular words"
    total = 0
    for word in words:
        if isTriangular(sum(alphabeticalPositions(word))):
            total += 1
    return total

print(timeit.timeit(codedTriangleNumbers, number = 1))