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
    cmd = input("Enter the command: ")
    if cmd == "down" or "left" or "right":
        print("CMD: ", cmd)
        move(cmd)
    else:
        # other command operation (rotate, instant drop)
        pass
    if game_over(board):
        return True
    else:
        return False

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

# Game Start
def main():
    gameover = False
    board = []
    for i in range(20):
        row = []
        for j in range(10):
            row.append(0)
        board.append(row)
    
    print_board(board)
    while(not gameover):
        gameover = turnover(board)

if __name__ == "__main__":
    main()