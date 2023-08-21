#import pygame

"""
Note:
    - This code will use a cartesian coordinate system (x,y).
      i.e. (0,0) is bottom left of the board.
"""

class Pawn:
    def __init__(self, x, y): # x,y are the starting coordinates
        self.pos = (x,y)
        self.properties = {"canIgnorePieces":False, "directionLocked":True}
        self.baseMoves = [[0, 2]] # will be changed to [0,1] following first move

class Rook:
    def __init__(self, x, y):
        self.pos = (x,y)
        self.properties = {"canIgnorePieces":False, "directionLocked":False}
        self.baseMoves = [[0, x] for x in range(1,8)] + [[x, 0] for x in range(-7,8)]

class Knight:
    def __init__(self, x, y):
        self.pos = (x,y)
        self.canIgnorePieces = True
        self.directionLocked = False
        self.baseMoves = [[2,1]]
        for i in range(0, 3):
            self.baseMoves.append((-self.baseMoves[-1][1],self.baseMoves[-1][0]))
        self.baseMoves += [(-move[0], move[1]) for move in self.baseMoves]

class Bishop:
    def __init__(self, x, y):
        self.pos = (x,y)
        self.canIgnorePieces = True
        self.directionLocked = False
        self.baseMoves = [[i,i] for i in range(-7,)]

class Chess:
    def __init__(self):
        self.playBoard = None; self.resetPlayBoard()
        self.tileBoard = None; self.createTileBoard()

    def resetPlayBoard(self): # board for players to play on. includes all pieces
        playBoardBase = [[2,3,4,5,6,4,3,2],
                 [1,1,1,1,1,1,1,1],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [7,7,7,7,7,7,7,7],
                 [8,9,10,11,12,10,9,8]]
    
    def createTileBoard(self): # describes board tile colours
        self.tileBoard = [[i % 2 for i in range(j,j+8)] for j in range(0, 8)]

    def possPawn(self, p):
        if self.playBoard[p[0], p[1]] not in [1,7]:
            return 0 # Input is not a pawn
        

game = Chess()
Knght = Knight(7,3)
print(Knght.baseMoves)