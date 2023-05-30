# import pygame
import random
import keyboard

blocks = ["I", "J", "L", "O", "S", "T", "Z"]
blocksShape = {"I":[[0,1,0,0],
                [0,1,0,0],
                [0,1,0,0],
                [0,1,0,0]],"J": [[0,1,0],
                            [0,1,0],
                            [1,1,0]],"L": [[1,0,0],
                                        [1,0,0],
                                        [1,1,0]],"O": [[1,1],
                                                    [1,1]],"S": [[0,1,1],
                                                                [1,1,0],
                                                                [0,0,0]],"T": [[0,1,0],
                                                                            [1,1,1],
                                                                            [0,0,0]],"Z": [[1,1,0],
                                                                                        [0,1,1],
                                                                                        [0,0,0]]}
block = ""

class block:
    def __init__(self, name):
        self.matrix = blocksShape[name]
        self.pos = [0,4]

def turnover(board):
    global block
    if block == "": 
        block = blocks[random.randint(0,6)]
        # place the block on top of the board
        print("Block:", block)
        spawnBlock(board, block)
    
    print_board(board)
        
    cmd = input("\nEnter the command: ")
    
    if (cmd.lower() == "down") or (cmd.lower() == "left") or (cmd.lower() == "right"):
        print("Move cmd: ", cmd.lower())
        move(cmd.lower())
    elif cmd == "":
        move("down")
    else:
        # other command operation (rotate, instant drop)
        if cmd.lower() == "drop":
            drop()
        pass
    
    return game_over(board)
    
def print_board(board):
    for i in range(len(board)):
        string = ""
        for j in range(len(board[i])):
            string += str(board[i][j]) + " "
        print(string)
        
def game_over(board):
    for i in range(10):
        if (board[20][i] == 1):
            return True
    return False

def move(cmd, block):
    pass

def rotate(cmd, block):
    pass

def drop(block):
    pass

def detectBlock(blockName):
    

def spawnBlock(board, block):
    actBlock = blocksShape[block]
    if actBlock != blocksShape["I"] and actBlock != blocksShape["O"]:
        for i in range(3):
            for j in range(3):
                board[i][j+4] = actBlock[i][j]
    elif actBlock == blocksShape["I"]:
        for i in range(4):
            for j in range(4):
                board[i][j+4] = actBlock[i][j]
    elif actBlock == blocksShape["O"]:
        for i in range(2):
            for j in range(2):
                board[i][j+4] = actBlock[i][j]
    pass

# Game Start
def main():
    gameover = False
    board = []
    for i in range(24):
        row = []
        for j in range(10):
            row.append(0)
        board.append(row)
    
    while(not gameover):
        gameover = turnover(board)

if __name__ == "__main__":
    main()