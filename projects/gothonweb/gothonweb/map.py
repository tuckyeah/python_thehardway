from random import randint 
from transitions import *

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
	
    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

class Death(Room):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud... if she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better than this."
    ]
    
    def __init__(self, description):
        self.name = "death"
        self.description = description
        # random quip for use in header
        self.quip = Death.quips[randint(0, len(self.quips)-1)]


central_corridor = Room("Central Corridor", cc_initial_description)


laser_weapon_armory = Room("Laser Weapon Armory", law_initial_description)


the_bridge = Room("The Bridge", bridge_initial_description)


escape_pod = Room("Escape Pod", pod_initial_description)


the_end_winner = Room("The End",
"""
You jump into pod 2 and hit the eject button.
The pod easily slides out into space heading to
the planet below. As it flies to the planet, you look
back and see your ship implode and explode like a
bright star, taking out the Gothon ship at the same
time.  You won!
""")


the_end_loser = Room("The End", 
"""
You jump into a random pod and hit the eject button.
The pod escapes out into the void of space, then
implodes as the hull ruptures, curshing your body
into jam jelly.
"""
)

# creating objects for each room's deaths
generic_death = Death("you died.")

cc_shoot_death = Death(cc_shoot_transition)
cc_dodge_death = Death(cc_dodge_transition)

law_death = Death(law_wrong_code)

bridge_death = Death(bridge_throw_death)

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

the_bridge.add_paths({
    'throw the bomb': bridge_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '0132': the_bridge,
    '*': law_death
})

central_corridor.add_paths({
    'shoot!': cc_shoot_death,
    'dodge!': cc_dodge_death,
    'tell a joke': laser_weapon_armory
})

START = central_corridor