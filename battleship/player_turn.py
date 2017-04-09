import Queue

def player_turn(player, enemy_fleet, enemy_board, previous_moves):
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
            print "Your opponent attacked " +  str(last_player_move.values()[0]) + " and hit your " +  str(last_player_move.keys()[0])
    print "It\'s your turn now, " + player.name
    print 
    print_board(enemy_board)
    # while loop controls player's turn
    turn_over = False
    while turn_over == False: 
        # Validate player coordinate input
        try: 
            guess_row = int(raw_input("Guess Row:"))
        except ValueError:
            print "That\'s not an integer value. Please enter a number from 1 to 10."
        try:
            guess_col_string = str(raw_input("Guess Col:"))
        except ValueError:
            print "What language is that? Please try entering a letter again."
        guess_col = letter_to_integer[guess_col_string]
        # check if player guess inside board
        if (guess_row < 1 or guess_row >= len(enemy_board)) or \
        (guess_col < 1 or guess_col >= len(enemy_board)):
            print "Oops, that's not even in the ocean! Please try again."
        # check if player guess previously guessed
        elif enemy_board[guess_row][guess_col] == "X" or enemy_board[guess_row][guess_col] == '*':
            print "You guessed that one already."
        # check if player guess is hit or miss then end turn
        else:          
            try:
                for ship in enemy_fleet:
                    for ship_row, ship_col in enemy_fleet[ship]:
                        if guess_row == ship_row and guess_col == ship_col:
                            raise
            except:
                enemy_board[guess_row][guess_col].is_hit = True
                print "You hit the enemy %s!" % (ship)
                enemy_fleet[ship].remove((ship_row, ship_col))
                if len(enemy_fleet[ship]) == 0:
                    print "You sunk the enemy " + ship + "!"
                previous_moves.put({ship : (guess_row, guess_col)})
                turn_over = True
            else:
                enemy_board[guess_row][guess_col].is_hit = True
                print "You missed!"
                previous_moves.put({'m' : (guess_row, guess_col)})
                turn_over = True



''' This needs to be combined with main() '''
def run(player1, player2):
    previous_moves = Queue.Queue(1)
    game_over = False
    while game_over == False:
        #
        #   Player 1 turn then check if Player 2 lost
        #
        player_turn(player1, player2.fleet, player2.board, previous_moves)
        player2_loss = fleet_destroyed(player2.fleet)
        if player2_loss:
            print Player2.name + "\'s fleet is destroyed! " + player1.name + " has won!"
            game_over == True
        #
        # Player 2 turn then check if Player 1 lost
        #    
        player_turn(player2, player1.fleet, player1.board, previous_moves)
        player1_loss = fleet_destroyed(player1.fleet)
        if player1_loss:
            print Player1.name + "\'s fleet is destroyed! " + player2.name + " has won!"
            game_over == True



