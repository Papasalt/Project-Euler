import numpy as np


path = "Number Grid.txt"

def importGridAsStr(path = "Number Grid.txt"):
    grid = []
    with open(path, "r") as file:
        #content = file.read()
        lines = file.readlines()
        for line in lines:
            grid.append(line.rstrip().split(" "))
    
    return grid

def removeInvalidNumbers(input_list):
    new_list = []
    new_line = []
    for line in input_list:
        for value in line:
            new_line.append(value[1:] if value[0] == "0" else value)
        new_list.append(new_line.copy())
        new_line.clear()
    return new_list

def convertAllToInt(input_list):
    for line_i in range(len(input_list)):
        input_list[line_i] = list(map(int, input_list[line_i]))
    return input_list


def prod(array_type):
    product = 1
    x_mem = None
    for x in array_type:
        product_mem = product
        product *= x
        #print(product)
        if product < 0:
            print("INTEGER OVERFLOW; LAST VALUES WERE: ", product_mem, "\t", x_mem)
    return product

grid = removeInvalidNumbers(importGridAsStr(path))
grid = convertAllToInt(grid)

def findLargestProductOfAdjacents(input_grid, max_distance, starting_pos): # POS INPUT MUST BE TUPLE TYPE
    adjacent_group = []
    largest_product_of_adjacents = -1
    directions = [(0, 1), (0, -1), (1, 1), (1, 0), 
                  (1, -1), (-1, 1), (-1, 0), (-1, -1)]
    for direction in directions:
        adjacent_group.clear()
        distance = 0
        current_pos = starting_pos
        y, x = current_pos[0], current_pos[1]
        while y >= 0 and x >= 0 and distance < max_distance:
            distance += 1
            y, x = current_pos[0], current_pos[1]
            try:
                adjacent_group.append(input_grid[y][x])
            except:
                break
            current_pos = tuple(np.add(current_pos, direction))
        print(adjacent_group, "\t", direction)
        product_of_adjacents = prod(adjacent_group)
        #print(product_of_adjacents)
        if product_of_adjacents > largest_product_of_adjacents:
            #print(product_of_adjacents, "\t", largest_product_of_adjacents)
            largest_product_of_adjacents = product_of_adjacents
    
    return largest_product_of_adjacents

def largestProductInGrid(grid, length):
    largest_product_of_adjacents_in_grid = 0
    largest_start = None
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            largest_product_of_adjacents = findLargestProductOfAdjacents(grid, length, (y, x))
            if largest_product_of_adjacents > largest_product_of_adjacents_in_grid:
                largest_start = grid[y][x]
                largest_product_of_adjacents_in_grid = largest_product_of_adjacents
    print(largest_start)
    return largest_product_of_adjacents_in_grid

print(largestProductInGrid(grid, 4))