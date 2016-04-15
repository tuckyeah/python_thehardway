from sys import exit
from random import randint

# the computer picks a 4 digit number, and keeps it hidden from the user
# the user has 10 tries to guess the number
# the computer will tell you if you get any of the numbers correct
# ideally if they are in the right place too

class Computer(object):

	def __init__(self):
		self.goal_number = []
		goal_string = goal_number.join()

	def pick_a_number(self):
		for i in range(0, 4):
			self.goal_number.append(randint(1,9))

	def print_number(self):
		print self.goal_number

	def guessed_numbers(self):
		# remove the correct number and return it?
		pass



class Player(object):
	
	def __init__(self):
		self.guessed_numbers = []
		self.correct_guesses = []
		self.guess = []

	def make_guess(self):
		guessed_num = raw_input("Guess a number >")

	def check_guess(self, guess):
		try:
			int(guess)
		except KeyError:
			print "Enter a number"
			self.make_guess()

		guessed_numbers.append(int(guess))
		return guessed_numbers


	def turn(self):
		# counter += 1
		pass


class Engine(object):

	def __init__(self):
		pass

	def check_turn(self, counter):
		pass

	def check_guess(self, guess):
		pass
