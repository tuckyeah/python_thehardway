from nose.tools import *
from gothonweb.map import *

def test_room():
    bridge = the_bridge
    assert_equal(bridge.name, "The Bridge")
    assert_equal(bridge.paths, {'throw the bomb': generic_death,
                              'slowly place the bomb': escape_pod})
	
def test_room_paths():
    central = central_corridor
    laser = laser_weapon_armory
	
    assert_equal(central.paths, {
        'shoot!': generic_death,
        'dodge!': generic_death,
        'tell a joke': laser_weapon_armory})
	
    assert_equal(laser.paths, {
        '0132': the_bridge,
        '*': generic_death})

def test_deaths():
    death_type = generic_death.description
    assert(death_type in QUIPS)
    assert(generic_death.description in QUIPS)
	
def test_gothon_game_map():
    assert_equal(START.go('shoot!'), generic_death)
    assert_equal(START.go('dodge!'), generic_death)

    room = START.go('tell a joke')
    assert_equal(room, laser_weapon_armory)