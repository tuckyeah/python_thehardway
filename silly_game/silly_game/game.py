from random import randint
from sys import exit

# make a guessing game with computer 
# computer picks four random colors from a list
# you guess different color combinations (with abbreviations)
# ideally the computer will also tell you if you have any 
# right colors, and any right colors in the right place(?)

COLORS = ["RED", "BLUE", "GREEN", "ORANGE", "WHITE", "YELLOW", 
        "PINK", "PURPLE"]


class Engine(object):

	def __init__(self):
		self.guessed = []
		self.cpu_colors = []


	def pick_colors(self):
		for n in range(0, 4):
			self.cpu_colors.append(COLORS[randint(0, len(COLORS)-1)])


	def print_all_colors(self):
		print self.guessed
		print self.cpu_colors


	def start_game(self):
		self.pick_colors()

		print "Let's play a game. Please pick four colors from the following:"
		print COLORS
		if len(self.guessed) > 0:
			print "/n"
			print "Guessed: "
			print self.guessed

		one_round = self.get_guess()

		self.check_guess(one_round)


	def get_guess(self):
		color_set = []
		
		for i in range(0, 4):
			color = raw_input("Pick a color: ")
			# add a check to make sure the input is valid
			# and in the dictionary
			
			color_set.append(color.upper())
			self.guessed.append(color.upper())
			
			if color.upper() == "EXIT":
				print "Goodbye."
				exit(0)
			elif color.upper() == "COMPUTER":
				self.print_all_colors()

		return color_set


	def check_guess(self, guess):
		if guess == self.cpu_colors:
			print "You won!"
			exit(0)
		
		if self.find_right_colors(guess):
			print "Right colors:"
			print self.right_colors
		else:
			print "No right colors."
		
		print "-" * 10
		self.start_game()

		
	def find_right_colors(self, guess):
		self.right_colors = []

		for i in guess:
			if i in self.cpu_colors:
				self.right_colors.append(i)

		return self.right_colors