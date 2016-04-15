from nose.tools import *
from silly_game.game import *
from sys import exit

game = Engine()

def test_pick_colors():

	game.pick_colors()

	assert_equal(len(game.cpu_colors), 4)

	for i in range(0,4):
		assert(game.cpu_colors[i] in COLORS)




def test_check_guess():

	game.cpu_colors = ["BLUE", "YELLOW", "PINK", "GREEN"]

	right_guess = ["BLUE", "YELLOW", "PINK", "GREEN"]
	wrong_guess = ["PURPLE", "BLUE", "WHITE", "RED"]

	with assert_raises(SystemExit) as cm:
		game.check_guess(right_guess)

	the_exception = cm.exception 
	assert_equal(the_exception.code, 0)
    


