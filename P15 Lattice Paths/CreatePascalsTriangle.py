""" To find number of paths in an n-sized square grid (lattice)
look for row 2n in pascals triangle, and the largest number if the number of
routes there are to get from top left to bottom right in the square.
E.g: A 20x20 sized grid.
n = 20
2n = 40
Search for the 40th row in pascals triangle
The largest number (center of row) is the number of routes, hence a 20x20
grid (lattice) has 137846528820 routes from top left to bottom right.
"""

def CreatePascalTriangle(max_row):
    rows = [[1], [1, 1]]
    for row_n in range(1, max_row):
        current_row = [1, 1]
        for i in range(0, row_n):
            #print(rows[row_n])
            x = rows[row_n][i] + rows[row_n][i+1]
            current_row.insert(i+1, x)
        rows.append(current_row)
    return rows

pascals_triangle = CreatePascalTriangle(199)
count = 0
count_entries = 0
for row in pascals_triangle:
    for entry in row:
        count_entries += 1
        if entry % 7 != 0:
            count += 1
print(count)
print(count_entries)