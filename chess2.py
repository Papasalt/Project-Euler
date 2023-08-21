"""
Coordinates stored as (y,x), where top left of the board is (0,0)
base_moves is stored as list of vectors (displacement from original position)
all getMoves functions are written from the perspective of black
"""

def isOutOfBounds(y,x):
    if not all([0<=y<8,0<=x<8]):
        return True
    return False

class Pawn:
    def __init__(self,colour,pos,move_n=0):
        self.colour = colour
        self.pos = pos
        self.move_n = move_n
    
    def getMoves(self,board):
        base_moves = []
        if self.colour == "white":
            pos = self.pos
            pos[0] = 7-self.pos[0]
            board = board[::-1]
        else:
            pos = self.pos
        
        if self.move_n == 0:
            base_moves.append((2,0))
        base_moves.append((1,0))
        
        p1 = board[pos[0]+1][pos[1]+1]
        if p1 != None and p1.colour != self.colour and not isOutOfBounds(pos[0]+1,pos[1]+1):
            base_moves.append((1,1))
        
        p2 = board[pos[0]+1][pos[1]-1]
        if p2 != None and p2.colour != self.colour and not isOutOfBounds(pos[0]+1,pos[1]-1):
            base_moves.append((1,-1))
        
        if self.colour == "white":
            base_moves = [(-t[0],t[1]) for t in base_moves]
        return base_moves
    
    def __repr__(self):
        return f"{self.colour[0]}_Pawn"

class Rook:
    def __init__(self,colour,pos):
        self.colour = colour
        self.pos = pos
    
    def getMoves(self,board):
        base_moves = []
        base_moves.extend([(y,0) for y in range(-7,8) if not isOutOfBounds(self.pos[0]+y,self.pos[1]) and y!=0])
        base_moves.extend([(0,x) for x in range(-7,8) if not isOutOfBounds(self.pos[0],self.pos[1]+x) and x!=0])
        return base_moves
    
    def __repr__(self):
        return f"{self.colour[0]}_Rook"

class Bishop:
    def __init__(self,colour,pos):
        self.colour = colour
        self.pos = pos
    
    def getMoves(self,board):
        base_moves = []
        base_moves.extend([(y,y) for y in range(-7,8) if not isOutOfBounds(self.pos[0]+y,self.pos[1]+y) and y!=0])
        base_moves.extend([(-y,y) for y in range(-7,8) if not isOutOfBounds(self.pos[0]-y,self.pos[1]+y) and y!=0])
        
        return base_moves
    
    def __repr__(self):
        return f"{self.colour[0]}_Bishop"

class Knight:
    def __init__(self,colour,pos):
        self.colour = colour
        self.pos = pos
    
    def getMoves(self,board):
        base_moves = [(2,1)]
        for i in range(0, 3):
            base_moves.append((-base_moves[-1][1],base_moves[-1][0]))
        base_moves += [(-move[0], move[1]) for move in base_moves]
        base_moves = [(t[0],t[1]) for t in base_moves if not isOutOfBounds(self.pos[0]+t[0],self.pos[1]+t[1])]
        return base_moves
    
    def __repr__(self):
        return f"{self.colour[0]}_Knight"

class Chess:
    def __init__(self):
        self.board = self.constructBoard()
    
    def printBoard(self):
        for row in self.board:
            print(row)
    
    def flippedBoard(self):
        return self.board[::-1]
    
    def constructBoard(self):
        board = [[None for i in range(0,8)] for j in range(0,8)]
        board[1] = [Pawn("black",[1,i]) for i in range(0,8)]
        board[0][0],board[0][7] = Rook("black",[0,0]), Rook("black",[0,7])
        board[0][2],board[0][5] = Bishop("black",[0,2]), Bishop("black",[0,5])
        board[0][1],board[0][6] = Knight("black",[0,1]), Knight("black",[0,6])
        
        board[6] = [Pawn("white",[6,i]) for i in range(0,8)]
        board[7][0],board[7][7] = Rook("white",[7,0]), Rook("white",[7,7]) 
        board[7][2],board[7][5] = Bishop("white",[7,2]), Bishop("white",[7,5])
        board[7][1],board[7][6] = Knight("white",[7,1]), Knight("white",[7,6])
        
        return board

Game = Chess()
Game.printBoard()
print(Game.board[0][1].getMoves(Game.board))