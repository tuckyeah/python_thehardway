from nose.tools import *
from numguessgame.game import *

computerTest = Computer()
playerTest = Player()

def test_computer_number():

	computerNumber = computerTest.pick_a_number()
	assert_equal(len(computerTest.goal_number), 4)
	
	for n in computerTest.goal_number:
		assert(n in range(1,9))



