import random, sys, Queue
import battleship_GUI



class Square():
    def __init__(self, coordinate):
        self.coordinate = coordinate
        # GUI
        self.xlocation = None
        self.ylocation = None
        self.img_length = 50
        # game logic
        self.hit = False
        self.miss = False

    def set_coordinate(self, x, y):
        self.xlocation = x
        self.ylocation = y

    def is_hit(self):
        self.hit = True

    def is_miss(self):
        self.miss = True

# function makes both players' boards given a board length
# returns dictionary -> keys = # coordinates, values = square obj's
# board_length unit: Square object
# img_length unit: pixel
def board_maker(board_length, img_length):
    # each player has two boards
    player1_board = {}
    player1_enemyBoard = {}
    player2_board = {} 
    player2_enemyBoard = {}
    # populates board maps with Square obj's
    for row in range(1, board_length + 1):
        for col in range(1, board_length + 1):
            player1_board[(row,col)] = Square((row,col))
            player1_enemyBoard[(row,col)] = Square((row,col))
            player2_board[(row,col)] = Square((row,col))
            player2_enemyBoard[(row,col)] = Square((row,col))
    # set rect.topleft x and y coordinates for Square obj's
    x = img_length
    y = img_length
    x2start = 2 * img_length + board_length * img_length
    x2 = x2start
    y2 = img_length
    for row in range(1, board_length + 1):
        if row != 1:
            x = img_length
            x2 = x2start
            y += img_length
            y2 += img_length
        for col in range(1, board_length + 1):
            player1_board[(row,col)].set_coordinate(x, y)
            player1_enemyBoard[(row,col)].set_coordinate(x2, y2)
            player2_board[(row,col)].set_coordinate(x, y)
            player2_enemyBoard[(row,col)].set_coordinate(x2, y2)
            x += img_length
            x2 += img_length
    return player1_board, player1_enemyBoard, player2_board, player2_enemyBoard


# Generates user friendly display for debugging
def print_board(board):
    for row in board:
        print " ".join(row)



