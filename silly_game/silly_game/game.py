from random import randint

# make a guessing game with computer 
# computer picks four random colors from a list
# you guess different color combinations (with abbreviations)
# ideally the computer will also tell you if you have any 
# right colors, and any right colors in the right place(?)

COLORS = ["RED", "BLUE", "GREEN", "ORANGE", "WHITE", "YELLOW", 
        "PINK", "PURPLE"]


class Computer(object):
	
	def __init__(self):
		self.cpu_colors = []

	def pick_colors(self):

		for n in range(0, 3):
			self.cpu_colors.append(COLORS[randint(0, len(COLORS)-1)])

	def print_colors(self):
		
		print self.cpu_colors


class Player(object):
	
	def __init__(self):
		
		self.guessed = []

	def get_guess(self):
		
		guess = raw_input("Guess a color: ")
		
		self.guessed.append(guess)

	def print_colors(self):
		
		print self.guessed


class Engine(object):

	def __init__(self):
		pass

	def print_all_colors(self):
		pass

	def start_game(self):
		pass

