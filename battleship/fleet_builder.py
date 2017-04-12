import random, board, math

###########################################################
#                       Fleet Builder
###########################################################

class Ship():
    def __init__(self):
        self.name = ""
        self.length = 0
        self.coordinate_list = {}
        self.image_list = {}

    def __delitem__(self, ship_part):
        del self.get_coordinate_list()[ship_part]
        del self.get_image_list()[ship_part]

    def get_coordinate_list(self):
        return self.coordinate_list

    def get_image_list(self):
        return self.image_list

    def get_coordinate(self, number):
        return self.coordinate_list[number]

    def get_length(self):
        return self.length

    # ship_part facilitates GUI 
    def set_coordinate(self, ship_part, (x,y)):
        self.coordinate_list[ship_part] = (x,y)  


class Destroyer(Ship):
    def __init__(self):
        Ship.__init__(self)
        self.name = "destroyer"
        self.length = 2
        self.coordinate_list[1] = (0,0)
        self.coordinate_list[2] = (0,0)

class Cruiser(Ship):
    def __init__(self):
        Ship.__init__(self)
        self.name = "cruiser"
        self.length = 3
        self.coordinate_list[1] = (0,0)
        self.coordinate_list[2] = (0,0)
        self.coordinate_list[3] = (0,0)
        # add GUI link soon

class Submarine(Ship):
    def __init__(self):
        Ship.__init__(self)
        self.name = "submarine"
        self.length = 3
        self.coordinate_list[1] = (0,0)
        self.coordinate_list[2] = (0,0)
        self.coordinate_list[3] = (0,0)
        # add GUI link soon


class Battleship(Ship):
    def __init__(self):
        Ship.__init__(self)
        self.name = "battleship"
        self.length = 4
        self.coordinate_list[1] = (0,0)
        self.coordinate_list[2] = (0,0)
        self.coordinate_list[3] = (0,0)
        self.coordinate_list[4] = (0,0)
        # add GUI link soon

class Carrier(Ship):
    def __init__(self):
        Ship.__init__(self)
        self.name = "carrier"
        self.length = 5
        self.coordinate_list[1] = (0,0)
        self.coordinate_list[2] = (0,0)
        self.coordinate_list[3] = (0,0)
        self.coordinate_list[4] = (0,0)
        self.coordinate_list[5] = (0,0)
        # add GUI link soon



def random_2tuple(board):
    row = random.randint(1, math.sqrt(len(board)))
    column = random.randint(1, math.sqrt(len(board)))
    return (row, column)



# Checks all four directions for board availability and other ship presence
# If board is available and no ship presence, builds
def direction_picker(player_board, current_ship, first_coordinate, player_fleet):
    possible_directions = []
    # checks up
    if first_coordinate[0] - (current_ship.get_length() - 1) >= 1:
        prospective_coordinates = []
        difference = 1 
        for i in range(current_ship.get_length() - 1):
            prospective_coordinates.append((first_coordinate[0] - difference, first_coordinate[1]))
            difference += 1
        try:     
            for ship in player_fleet:
                coordinate_list = player_fleet[ship].get_coordinate_list()
                for key in coordinate_list:
                    if coordinate_list[key] in prospective_coordinates:
                        raise
        except:
            pass
        else:
            possible_directions.append('up')
    # check right
    if first_coordinate[1] + (current_ship.get_length() - 1) <= math.sqrt(len(player_board)):
        prospective_coordinates = []
        difference = 1 
        for i in range(current_ship.get_length() - 1):
            prospective_coordinates.append((first_coordinate[0], first_coordinate[1] + difference))
            difference += 1
        try:     
            for ship in player_fleet:
                coordinate_list = player_fleet[ship].get_coordinate_list()
                for key in coordinate_list:
                    if coordinate_list[key] in prospective_coordinates:
                        raise 
        except:
            pass
        else:
            possible_directions.append('right')
    # check down
    if first_coordinate[0] + (current_ship.get_length() - 1) <= math.sqrt(len(player_board)):
        prospective_coordinates = []
        difference = 1 
        for i in range(current_ship.get_length() - 1):
            prospective_coordinates.append((first_coordinate[0] + difference, first_coordinate[1]))
            difference += 1
        try:     
            for ship in player_fleet:
                coordinate_list = player_fleet[ship].get_coordinate_list()
                for key in coordinate_list:
                    if coordinate_list[key] in prospective_coordinates:
                        raise 
        except:
            pass
        else:
            possible_directions.append('down')
    # check left 
    if first_coordinate[1] - (current_ship.get_length() - 1) >= 1:
        prospective_coordinates = []
        difference = 1 
        for i in range(current_ship.get_length() - 1):
            prospective_coordinates.append((first_coordinate[0], first_coordinate[1] - difference))
            difference += 1
        try:     
            for ship in player_fleet:
                coordinate_list = player_fleet[ship].get_coordinate_list()
                for key in coordinate_list:
                    if coordinate_list[key] in prospective_coordinates:
                        raise 
        except:
            pass
        else:
            possible_directions.append('left')
    # selects random direction 
    direction = random.choice(possible_directions)
    return direction


# Adds coordinates to ship object
# First, validates & builds random coordinate 
# Second, validates & builds in random direction from first coordinate
def ship_builder(player_board, current_ship, player_fleet):
    # validates & builds random coordinate
    uniqueness = False    
    while uniqueness != True:
        random_coordinate = random_2tuple(player_board)
        try:
            for ship in player_fleet:
                coordinate_list = player_fleet[ship].get_coordinate_list()
                for coordinate in coordinate_list:
                    if coordinate_list[coordinate] == random_coordinate:
                        raise
        except:
            pass
        else: 
            current_ship.set_coordinate(1, random_coordinate)
            uniqueness = True

    # validates & builds in random direction
    first_coordinate = current_ship.get_coordinate(1)
    direction = direction_picker(player_board, current_ship, first_coordinate, player_fleet)
    if direction == 'up':
        difference = 1
        ship_part = difference + 1
        for i in range(current_ship.get_length() - 1):
            current_ship.set_coordinate(ship_part, (first_coordinate[0] - difference, first_coordinate[1]))
            difference += 1
            ship_part += 1
    elif direction == 'down':
        difference = 1
        ship_part = difference + 1
        for i in range(current_ship.get_length() - 1):
            current_ship.set_coordinate(ship_part, (first_coordinate[0] + difference, first_coordinate[1]))
            difference += 1
            ship_part += 1
    elif direction == 'left':
        difference = 1
        ship_part = difference + 1
        for i in range(current_ship.get_length() - 1):
            current_ship.set_coordinate(ship_part, (first_coordinate[0], first_coordinate[1]- difference ))
            difference += 1
            ship_part += 1
    elif direction == 'right':
        difference = 1
        ship_part = difference + 1
        for i in range(current_ship.get_length() - 1):
            current_ship.set_coordinate(ship_part, (first_coordinate[0], first_coordinate[1]+ difference ))
            difference += 1
            ship_part += 1


# builds fleet by calling ship_builder()
def fleet_builder(player_board):
    # instantiates ships
    player_fleet = {}
    player_fleet["destroyer"] = Destroyer()
    player_fleet["cruiser"] = Cruiser()
    player_fleet["submarine"] = Submarine()
    player_fleet["battleship"] = Battleship()
    player_fleet["carrier"] = Carrier()
    for ship in player_fleet:
        ship_builder(player_board, player_fleet[ship], player_fleet)
    return player_fleet
