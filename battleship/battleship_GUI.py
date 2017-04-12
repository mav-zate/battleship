import os, pygame, math
from pygame.locals import *


# main directories
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")
first_row_dir = os.path.join(data_dir, "first_row")
first_col_dir = os.path.join(data_dir, "first_col")


# functions to create resources
def load_image(file_dir, name, colorkey=None):
	fullname = os.path.join(file_dir, name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error:
		print "Cannot load image: " + fullname
		raise SystemExit(str(get_error()))
	image = image.convert()
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
	return image

def load_sound(file_dir, name):
	class NoneSound:
		def play(self): pass
	if not pygame.mixer or not pygame.mixer.get_init():
		return NoneSound()
	fullname = os.path.join(file_dir, name)
	try:
		sound = pygame.mixer.Sound(fullname)
	except pygame.error:
		print ('Cannot load sound: %s' % fullname)
		raise SystemExit(str(get_error()))
	return sound


# connects GUI to internal board
class GUI():
	def __init__(self, player1_fleet, player1_board, player1_enemyBoard, \
	 player2_fleet, player2_board, player2_enemyBoard):

		self.square_length = player1_board[(1,1)].img_length
		self.board_length = self.square_length * 10 
		self.screen_height = player1_board[(1,1)].img_length * 14 # 700px
		self.screen_width = player1_board[(1,1)].img_length * 23 # 1150px
		

		# initializes display
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		pygame.display.set_caption("Battleship")
		self.background.fill((120,120,120))

		self.main_menu_pic = load_image(data_dir, "main_menu.png", None)
		self.start_pic1 = load_image(data_dir, "start_player_one.png", None)
		self.start_pic2 = load_image(data_dir, "start_player_two.png", None)
		self.victory_player_one = load_image(data_dir, "victory_player_one.png", None)
		self.victory_player_two = load_image(data_dir, "victory_player_two.png", None) 

		self.player1_board = player1_board
		self.player1_enemyBoard = player1_enemyBoard
		self.player2_board = player2_board
		self.player2_enemyBoard = player2_enemyBoard
		
		# board images
		self.water = load_image(data_dir, "blockSky.png", None)
		self.explosion = load_image(data_dir, "fire.png", (255,255,255))
		self.splash = load_image(data_dir, "splash.png", (255,255,255))

		# sounds
		self.kaboom = load_sound(data_dir, "kaboom.wav")
		self.sploosh = load_sound(data_dir, "sploosh.wav")
		# first row and column3
		self.first_row = {}
		self.first_col = {}
		# player fleets
		self.player1_fleet = player1_fleet
		self.player2_fleet = player2_fleet

	def render_main_menu(self):
		self.screen.blit(self.background, (0,0))
		self.screen.blit(self.main_menu_pic, (0,0))
		pygame.display.flip()


	def render_start_image1(self):
		self.screen.blit(self.background, (0,0))
		self.screen.blit(self.start_pic1, (0,0))
		pygame.display.flip()

	def render_start_image2(self):
		self.screen.blit(self.background, (0,0))
		self.screen.blit(self.start_pic2, (0,0))
		pygame.display.flip()

	def render_victory_player_one(self):
		self.screen.blit(self.background, (0,0))
		self.screen.blit(self.victory_player_one, (0,0))
		pygame.display.flip()
		
	def render_victory_player_two(self):
		self.screen.blit(self.background, (0,0))
		self.screen.blit(self.victory_player_two, (0,0))
		pygame.display.flip()	



	#load images for player1_fleet & player2_fleet
	def load_fleets(self):
		for ship in self.player1_fleet:
			coordinate_list_1 = self.player1_fleet[ship].get_coordinate_list()
			coordinate_list_2 = self.player2_fleet[ship].get_coordinate_list()
			for ship_part in coordinate_list_1:
				self.player1_fleet[ship].image_list[ship_part] = load_image(data_dir, ship + "_" + str(ship_part) + ".png", None)
			for ship_part in coordinate_list_2:
				self.player2_fleet[ship].image_list[ship_part] = load_image(data_dir, ship + "_" + str(ship_part) + ".png", None)

	def load_board_label(self):
		# load images
		count = 1
		for col in range(1, 11):
			self.first_row[count] = load_image(first_row_dir, "first_row_" + str(count) + ".png", None)
			self.first_col[count] = load_image(first_col_dir, "first_column_" + str(count) + ".png", None)
			count += 1


	# flip individual ship images according to orientation
	def correct_fleet_images(self, player_fleet):
		for ship in player_fleet:
			coordinate_list = player_fleet[ship].get_coordinate_list()
			image_list = player_fleet[ship].get_image_list()
			# ship picks 'up' direction
			if coordinate_list[2][0] == coordinate_list[1][0] - 1:
				for ship_part in image_list:
					image_list[ship_part] = pygame.transform.rotate(image_list[ship_part], 90)
			# ship picks 'down' direction
			elif coordinate_list[2][0] == coordinate_list[1][0] + 1:
				for ship_part in image_list:
					image_list[ship_part] = pygame.transform.rotate(image_list[ship_part], - 90)
			# ship picks 'left' direction
			elif coordinate_list[2][1] == coordinate_list[1][1] - 1:
				for ship_part in image_list:
					image_list[ship_part] = pygame.transform.flip(image_list[ship_part], 1, 0)
			else:
				pass


	def render_fleet1(self):
		for ship in self.player1_fleet:
			coordinate_list = self.player1_fleet[ship].get_coordinate_list()
			image_list = self.player1_fleet[ship].get_image_list()
			for ship_part in image_list:
				self.screen.blit(image_list[ship_part], \
				 (coordinate_list[ship_part][1] * self.square_length, coordinate_list[ship_part][0] * self.square_length) )
			for square in self.player1_board:
				if self.player1_board[square].hit:
					self.screen.blit(self.explosion, \
						(self.player1_board[square].xlocation, self.player1_board[square].ylocation))



	def render_fleet2(self):
		for ship in self.player2_fleet:
			coordinate_list = self.player2_fleet[ship].get_coordinate_list()
			image_list = self.player2_fleet[ship].get_image_list()
			for ship_part in image_list:
				self.screen.blit(image_list[ship_part], \
				 (coordinate_list[ship_part][1] * self.square_length, coordinate_list[ship_part][0] * self.square_length) )
			for square in self.player2_board:
				if self.player2_board[square].hit:
					self.screen.blit(self.explosion, \
						(self.player2_board[square].xlocation, self.player2_board[square].ylocation))

	def render_board_label(self):
		count = 1 
		x = self.square_length
		y = 0
		origin2 = 2 * self.square_length + self.board_length 
		x2 = origin2 + self.square_length
		while count < 11:
			# render first board label
			self.screen.blit(self.first_row[count], (x,y))
			self.screen.blit(self.first_col[count], (y,x))

			# render second board top label
			self.screen.blit(self.first_row[count], (x2,y))

			# render second board side label
			self.screen.blit(self.first_col[count], (origin2,x))

			# increment
			x += self.square_length
			x2 += self.square_length
			count += 1


	def render_board1(self):
		# displays background
		self.screen.blit(self.background, (0,0))
		# render each player's boards
		for square in self.player1_board:
			self.screen.blit(self.water, \
			 (self.player1_board[square].xlocation, self.player1_board[square].ylocation))
			# if hit by enemy
			if self.player1_board[square].hit:
				self.screen.blit(self.explosion, (self.player1_board[square].xlocation, self.player1_board[square].ylocation))
		for square in self.player1_enemyBoard:
			self.screen.blit(self.water, \
			 (self.player1_enemyBoard[square].xlocation, self.player1_enemyBoard[square].ylocation))
			# if player missed enemy
			if self.player1_enemyBoard[square].miss:
				self.screen.blit(self.splash, \
				 (self.player1_enemyBoard[square].xlocation, self.player1_enemyBoard[square].ylocation))
			# if player hit enemy
			elif self.player1_enemyBoard[square].hit:
				self.screen.blit(self.explosion, \
				 (self.player1_enemyBoard[square].xlocation, self.player1_enemyBoard[square].ylocation))


	def render_board2(self):
		# displays background
		self.screen.blit(self.background, (0,0))
		for square in self.player2_board:
			self.screen.blit(self.water, (self.player2_board[square].xlocation, self.player2_board[square].ylocation))
			# if hit by enemy
			if self.player2_board[square].hit:
				self.screen.blit(self.explosion, \
				 (self.player2_board[square].xlocation, self.player2_board[square].ylocation))
		for square in self.player2_enemyBoard:
			self.screen.blit(self.water, \
			 (self.player2_enemyBoard[square].xlocation, self.player2_enemyBoard[square].ylocation))
			# if player missed enemy
			if self.player2_enemyBoard[square].miss:
				self.screen.blit(self.splash, \
				 (self.player2_enemyBoard[square].xlocation, self.player2_enemyBoard[square].ylocation))
			# if player hit enemy
			elif self.player2_enemyBoard[square].hit:
				self.screen.blit(self.explosion, \
				 (self.player2_enemyBoard[square].xlocation, self.player2_enemyBoard[square].ylocation))
