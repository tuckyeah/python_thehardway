from nose.tools import *
from silly_game.game import *

cpu = Computer()


def test_pick_colors():

	cpu.pick_colors()

	assert_equal(len(cpu.cpu_colors), 3)

	for i in range(0,3):
		assert(cpu.cpu_colors[i] in COLORS)



