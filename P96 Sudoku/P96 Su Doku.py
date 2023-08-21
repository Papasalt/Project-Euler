import sys
sys.setrecursionlimit(10000)

def importGrids(path):
    grids = []
    grid = []
    with open(path) as file:
        lines = list(file.readlines())
        lines = [line.replace("\n","") for line in lines if line[0] != "G"]
        for i in range(0,len(lines)):
            if i % 9 == 0:
                grids.append(grid)
                grid = []
            grid.append(list(map(int,list(lines[i]))))
        grids.append(grid)
        del grids[0]
    return grids
grids = importGrids("p096_sudoku.txt")

example_grid = [[0,0,3,0,2,0,6,0,0],
                [9,0,0,3,0,5,0,0,1],
                [0,0,1,8,0,6,4,0,0],
                [0,0,8,1,0,2,9,0,0],
                [7,0,0,0,0,0,0,0,8],
                [0,0,6,7,0,8,2,0,0],
                [0,0,2,6,0,9,5,0,0],
                [8,0,0,2,0,3,0,0,9],
                [0,0,5,0,1,0,3,0,0]]

def slicer(array,a,b): # slices rectangle from given array, as marked by tuples a and b
    return [[array[y][x] for x in range(a[1],b[1]+1)] for y in range(a[0],b[0]+1)]

def printGrid(grid):
    [print(row) for row in grid]

class SolveSudoku:
    def __init__(self):
        pass
    
    def isInColumn(self,pos,n):
        for y in self.grid:
            if n == y[pos[1]]:
                return True
        return False
    
    def isInRow(self,pos,n):
        if n in self.grid[pos[0]]:
            return True
        return False
    
    def isInSubgrid(self,pos,n):
        a = (pos[0]-(pos[0]%3), pos[1]-(pos[1]%3))
        b = (pos[0]-(pos[0]%3)+2, pos[1]-(pos[1]%3)+2)
        subgrid = slicer(self.grid, a, b)
        for y in subgrid:
            if n in y:
                return True
        return False

    def isValid(self,pos,n):
        if any([self.isInColumn(pos,n),self.isInRow(pos,n),self.isInSubgrid(pos,n)]):
            return False
        return True

    def solve(self,i=0):
        if i == len(self.variables):
            #sys.exit()
            return self.grid
        p = self.variables[i]
        start = self.grid[p[0]][p[1]]
        for x in range(start+1,10):
            if self.grid in self.grid_history:
                print(p, i, x)
                printGrid(self.grid)
            if self.isValid(p,x):
                self.grid[p[0]][p[1]] = x
                self.grid_history.append(self.grid)
                break
        else:
            self.grid[p[0]][p[1]] = 0
            self.solve(i-1)
            return self.grid
        self.solve(i+1)
        return self.grid
    
    def startSolve(self,grid):
        try:
            self.grid = grid
            self.variables = [(i//9,i%9) for i in range(0,81) if self.grid[i//9][i%9] == 0]
            self.grid_history = [self.grid]
        except:
            print(grid)
        return self.solve()

def P96():
    total = 0
    Solver = SolveSudoku()
    for grid in grids:
        print(grid)
        solution = Solver.startSolve(grids[2])
        total += int("".join(list(map(str,solution[0][:3]))))
    return total

#print(P96())

Solver = SolveSudoku()
solution = Solver.startSolve(grids[2])