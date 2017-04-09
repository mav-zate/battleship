import random, sys, Queue, pygame, math, time
import battleship_GUI, player_turn, fleet_builder, board
from pygame.locals import *


'''
TO-DO:
    ---1. Add event handling so that you can add screen between 
        player turns
    ---2. add mini enemy version of player boards 
    ---3. Add explosions instead of deleting ship parts
    4. Add sound   
    5. add text so players understand how to play
'''

'''
NOTES:
    1. Player should be notified of sinking of enemy ship
    2. Game does not end when any fleet is sunk
    3. Exception handling: more than one letter input
    4. Add ending screen to congratulate playerx on win
'''



###########################################################
#
# created mav_zate
#
# This battleship code is for a game of battleship
#
# Number of Players:
# 
# Number, kind, and size of ships per player: five
#           Carrier: 5 
#           Battleship: 4 
#           Cruiser: 3 
#           Submarine: 3 
#           Destroyer: 2
#
#
# Number of guesses (single player): 10
#
#
# 
###########################################################
#
# 1. Main function (main loop that controls flow of game)
# 2. Ship instantiator folder and fleet status
# 3. logic of game
# 
#
#
#

# initializes 10 x 10 board 
#
# O means untouched space
# X means miss
# * means hit 
#

###########################################################
#                       Boards 
###########################################################
 

# dictionary used to create first row and first column
integer_to_letter = {
    1 : 'a',
    2 : 'b',
    3 : 'c',
    4 : 'd',
    5 : 'e',
    6 : 'f',
    7 : 'g',
    8 : 'h',
    9 : 'i',
    10 : 'j',
    11 : 'k',
    12 : 'l',
    13 : 'm',
    14 : 'n',
    15 : 'o', 
    16 : 'p',
    17 : 'q',
    18 : 'r',
    19 : 's',
    20 : 't',
    21 : 'u',
    22 : 'v',
    23 : 'w',
    24 : 'x',
    25 : 'y',
    26 : 'z'
}

# same as previous dictionary but with keys and indexes switchesd
letter_to_integer = {}
for integer in integer_to_letter:
    letter_to_integer[integer_to_letter.get(integer)] = integer






###########################################################
#                       Player Instantiation
###########################################################

class Player:
    def __init__(self, name, fleet, board):
        self.name = name
        self.fleet = fleet
        self.board = board





player1_board, player1_enemyBoard, player2_board, player2_enemyBoard = board.board_maker(10, 50)

player1_fleet = fleet_builder.fleet_builder(player1_board)
player2_fleet = fleet_builder.fleet_builder(player2_board)

player1 = Player("Maverick", player1_fleet, player1_board)
player2 = Player("Araz", player2_fleet, player2_board)

###########################################################




def fleet_destroyed(player_fleet, player_board):
    fleet = player_fleet
    # create fleet length variable
    fleet_length = 0
    for ship in fleet:
        fleet_length += fleet[ship].length
    sd = 0 # ship parts destroyed
    for ship in fleet:
        cl = fleet[ship].get_coordinate_list() # ship's coordinate list
        for ship_part in cl:
            if player_board[cl[ship_part]].hit:
                sd += 1
    if sd == fleet_length:
        return True
    else:
        return False










def main(player1, player2):
    # initialize pygame and GUI
    pygame.init()
    pygame.mixer.init()
    graphics = battleship_GUI.GUI(player1_fleet, player1_board, player1_enemyBoard, \
        player2_fleet, player2_board, player2_enemyBoard)
    # load all images
    graphics.load_board_label()
    graphics.load_fleets()
    # correct fleet images
    graphics.correct_fleet_images(player1_fleet)
    graphics.correct_fleet_images(player2_fleet)

    previous_moves = Queue.Queue(1)
    game_over = False
    turn = 1
    while game_over == False:
        ##############################################
        #                                            #
        #  Player 1 turn then check if Player 2 lost #
        #                                            #
        ##############################################

        if turn == 1:
            pygame.display.flip()             
            graphics.render_start_image1()
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_over = True    
                elif event.type == KEYDOWN and event.key == K_n:
                    # render Player 1 board 
                    graphics.render_board1()
                    graphics.render_board_label()
                    graphics.render_fleet1()
                    pygame.display.flip()
                    # player 1 events
                    player_turn(player1, graphics.player1_enemyBoard, graphics.player2_fleet,
                     graphics.player2_board, previous_moves, graphics)
                    player2_loss = fleet_destroyed(graphics.player2_fleet, graphics.player2_board)
                    if player2_loss:
                        print player2.name + "\'s fleet is destroyed! " + player1.name + " has won!"
                        game_over == True
                    turn = 2

        ##############################################
        #                                            #
        #  Player 2 turn then check if Player 1 lost #
        #                                            #
        ##############################################

        elif turn == 2:
            pygame.display.flip()
            graphics.render_start_image2()
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_over = True  
                elif event.type == KEYDOWN and event.key == K_m:
                    # render Player 2 board
                    pygame.display.flip()
                    graphics.render_board2()
                    graphics.render_board_label()
                    graphics.render_fleet2()
                    pygame.display.flip()
                    # player 2 events
                    player_turn(player2, graphics.player2_enemyBoard, graphics.player1_fleet,
                        graphics.player1_board, previous_moves, graphics)
                    player1_loss = fleet_destroyed(graphics.player1_fleet, graphics.player1_board)
                    if player1_loss:
                        print player1.name + "\'s fleet is destroyed! " + player2.name + " has won!"
                        game_over == True
                    turn = 1


        

        pygame.display.flip()


    pygame.quit()



def player_turn(player, player_enemyBoard, enemy_fleet, enemy_board, previous_moves, gui):
    ###########################################################
    # for debugging
    print enemy_fleet
    ###########################################################
    try:
        last_player_move = previous_moves.get(True,0.1)
    except:
        pass
    else:
        if last_player_move.has_key('m'):
            print "Your opponent attacked " + str(last_player_move['m']) + ", thus missing you."
        else:
            print "Your opponent attacked %s and hit your %s!" \
            % (str(last_player_move.values()[0]), str(last_player_move.keys()[0])) 
    print "It\'s your turn now, %s" % (player.name)
    
    # print board.print_board(enemy_board)
    # while loop controls player's turn
    turn_over = False
    while turn_over == False: 

        # Validate player coordinate input
        invalid_row = True
        while invalid_row:
            guess_row = str(raw_input("Guess Row:"))
            if not guess_row.isalpha():
                print "What language is that? Please try entering a letter again."
            else:
                invalid_row = False

        invalid_col = True
        while invalid_col:
            try:
                guess_col = int(raw_input("Guess Col:"))
            except ValueError:
                print "That\'s not an integer value. Please enter a number from 1 to 10."
            else:
                invalid_col = False
        guess_row = letter_to_integer[guess_row]

        # check if player guess inside board
        if (guess_row < 1 or guess_row > math.sqrt(len(enemy_board))) or \
        (guess_col < 1 or guess_col > math.sqrt(len(enemy_board))):
            print "Oops, that's not even in the ocean! Please try again."

        # check if player guess previously guessed
        elif enemy_board[(guess_row, guess_col)].hit:
            print "You guessed that one already."

        # check if player guess is hit or miss then end turn
        else:          
            try:
                for ship in enemy_fleet:
                    coordinate_list = enemy_fleet[ship].get_coordinate_list()
                    for ship_part in coordinate_list:
                        if coordinate_list[ship_part][0] == guess_row and coordinate_list[ship_part][1] == guess_col:
                            raise
            except:
                enemy_board[(guess_row,guess_col)].is_hit()
                player_enemyBoard[(guess_row,guess_col)].is_hit()
                gui.kaboom.play()
                time.sleep(1)
                print "You hit the enemy %s!" % (enemy_fleet[ship].name)
                if len(coordinate_list) == 0:
                    print "You sunk the enemy %s!" % (enemy_fleet[ship].name)
                previous_moves.put({enemy_fleet[ship].name : (guess_row, guess_col)})
                turn_over = True
            else:
                player_enemyBoard[(guess_row,guess_col)].is_miss()
                gui.sploosh.play()
                time.sleep(1)
                print "You missed!"
                previous_moves.put({'m' : (guess_row, guess_col)})
                turn_over = True


main(player1, player2)







        


