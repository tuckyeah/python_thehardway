#from nose.tools import *
#from gothonweb.map import *
#from gothonweb.transitions import *

QUIPS = [
    "You died. You kinda suck at this.",
    "Your mom would be proud... if she were smarter.",
    "Such a loser.",
    "I have a small puppy that's better than this."
]

def test_room():
    bridge = the_bridge
    assert_equal(bridge.name, "The Bridge")
    assert_equal(bridge.paths, {'throw the bomb': bridge_death,
                              'slowly place the bomb': escape_pod})

    escape = escape_pod
    assert_equal(escape.name, "Escape Pod")
    assert_equal(escape.paths, {'2': the_end_winner,
                                '*': the_end_loser})

def test_winner():
    winner = the_end_winner
    assert_equal(the_end_winner.name, "The End")
    assert_equal(the_end_winner.description, """
You jump into pod 2 and hit the eject button.
The pod easily slides out into space heading to
the planet below. As it flies to the planet, you look
back and see your ship implode and explode like a
bright star, taking out the Gothon ship at the same
time.  You won!
""")

def test_room_paths():
    central = central_corridor
    laser = laser_weapon_armory
	
    assert_equal(central.paths, {
        'shoot!': shoot_transition,
        'dodge!': dodge_transition,
        'tell a joke': laser_weapon_armory})
	
    assert_equal(laser.paths, {
        '0132': the_bridge,
        '*': law_death})

def test_deaths():
    death_test = Death("You Suck")
    assert(death_test.quip in QUIPS)
    assert_equal(death.description, "You Suck")
	
def test_gothon_game_map():
    assert_equal(START.go('shoot!'), shoot_transition)
    assert_equal(START.go('dodge!'), dodge_transition)

    room = START.go('tell a joke')
    assert_equal(room, laser_weapon_armory)