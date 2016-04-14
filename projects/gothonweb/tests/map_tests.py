from nose.tools import *
from gothonweb.map import *
from gothonweb.transitions import *

QUIPS = [
    "You died. You kinda suck at this.",
    "Your mom would be proud... if she were smarter.",
    "Such a loser.",
    "I have a small puppy that's better than this."
]

def test_room():
    centralcorridor = central_corridor

    assert_equal(centralcorridor.name, "Central Corridor")
    assert_equal(centralcorridor.description, cc_initial_description)
    assert_equal(centralcorridor.paths, {
        'shoot!': cc_shoot_death,
        'dodge!': cc_dodge_death,
        'tell a joke': laser_weapon_armory
        })

    laser = laser_weapon_armory

    assert_equal(laser.name, "Laser Weapon Armory")
    assert_equal(laser.description, law_initial_description)
    assert_equal(laser.paths, {
        '0132': the_bridge,
        '*': law_death
        })

    bridge = the_bridge

    assert_equal(bridge.name, "The Bridge")
    assert_equal(bridge.description, bridge_initial_description)
    assert_equal(bridge.paths, {
        'throw the bomb':  bridge_death,
        'slowly place the bomb': escape_pod
        })

    escape = escape_pod

    assert_equal(escape.name, "Escape Pod")
    assert_equal(escape.description, pod_initial_description)
    assert_equal(escape.paths, {
        '2': the_end_winner,
        '*': the_end_loser
        })


def test_winner():
    winner = the_end_winner

    assert_equal(winner.name, "The End")
    assert_equal(winner.description, winner_text)


def test_loser():
    loser = the_end_loser

    assert_equal(loser.name, "The End")
    assert_equal(loser.description, loser_text)


def test_death():
    deaths = [cc_shoot_death, cc_dodge_death, law_death, bridge_death]

    for i in deaths:
        assert(i.quip in QUIPS)
        assert_equal(i.name, "death")

    assert_equal(cc_shoot_death.description, cc_shoot_transition)
    assert_equal(cc_dodge_death.description, cc_dodge_transition)

    assert_equal(law_death.description, law_wrong_code)

    assert_equal(bridge_death.description, bridge_throw_death)


def test_gothon_game_map():
    assert_equal(START.go('shoot!'), cc_shoot_death)
    assert_equal(START.go('dodge!'), cc_dodge_death)

    room = START.go('tell a joke')
    assert_equal(room, laser_weapon_armory)

    lasers = laser_weapon_armory

    assert_equal(lasers.go('0132'), the_bridge)
    assert_equal(lasers.go('1222'), None)

    bridge = the_bridge

    assert_equal(bridge.go('throw the bomb'), bridge_death)
    assert_equal(bridge.go('slowly place the bomb'), escape_pod)

    escape = escape_pod

    assert_equal(escape.go('2'), the_end_winner)
    assert_equal(escape.go('7'), None)