# import pygame
import random
import keyboard

blocks = ["I", "J", "L", "O", "S", "T", "Z"]
block = ""

def turnover(board):
    global block
    if block == "": 
        block = blocks[random.randint(0,6)]
        # place the block on top of the board
        print("Block:", block)
        spawnBlock(board)
        
    cmd = input("\nEnter the command: ")
    
    if (cmd == "down") or (cmd == "left") or (cmd == "right"):
        print("Move cmd: ", cmd)
        move(cmd)
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
    return False

def move(cmd):
    pass

def rotate(cmd):
    pass

def drop():
    pass

def spawnBlock(board):
    pass

# Game Start
def main():
    gameover = False
    board = []
    for i in range(20):
        row = []
        for j in range(10):
            if i == 1: row.append(1)
            else: row.append(0)
        board.append(row)
    
    print_board(board)
    
    while(not gameover):
        gameover = turnover(board)
        print_board(board)

if __name__ == "__main__":
    main()