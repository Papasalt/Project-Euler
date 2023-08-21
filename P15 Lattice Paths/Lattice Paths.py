import math
import numpy as np

class Lattice:
    def __init__(self, size): #(tuple)lattice_size
        self.size = size
        self.size_x = size[1]
        self.size_y = size[0]
        self.lattice = np.zeros(size)
        self.pos = (0, 0)
    
    def east(self, distance):
        pos = list(self.pos)
        pos[1] += distance
        pos = tuple(pos)
        return pos
    
    def south(self, distance):
        pos = list(self.pos)
        pos[0] += distance
        pos = tuple(pos)
        return pos
    
    def numberOfPaths(self):
        explored_paths = []
        current_path = []
        run = 0
        while True:
            while self.pos != (self.size_y-1, self.size_x-1):
                print(self.pos)
                if self.east(1)[1] < self.size_x:
                    if run > 0: # If run > 0, then explored_paths will not be empty
                        if self.east(1) in explored_paths[-1]:
                            self.pos = self.east(1)
                            current_path.append(self.pos)
                    else:
                        self.pos = self.east(1)
                        current_path.append(self.pos)
                elif self.south(1)[0] < self.size_y:
                    if run > 0: # If run > 0, then explored_paths will not be empty
                        if self.south() in explored_paths[-1]:
                            self.pos = self.south(1)
                            current_path.append(self.pos)
                    else:
                        self.pos = self.south(1)
                        current_path.append(self.pos)
            explored_paths.append(current_path)
            run += 1
            for i, e in enumerate(current_path):
                print(i, e)
            break
        print(explored_paths)


LatticePaths = Lattice((3, 3))
print(LatticePaths.lattice)
LatticePaths.numberOfPaths()