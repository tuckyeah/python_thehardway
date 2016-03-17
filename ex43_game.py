# import 'exit' function from sys module
from sys import exit
# import 'randint' function from random module
from random import randint

# defining a class called "Scene," which all of the rooms will inherit from
# So it contains all the common functions for all the rooms
class Scene(object):
	# This function will be overwritten in every instance, so this is a placeholder
	# In a more complicated program, there would be more functions here
	# Not all of which would be overwritten (presumably)
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

# defining a function called 'Engine' which will control how we move through
# the rooms.  		
class Engine(object):
	
	#initializes the object with scene_map as an argument
    def __init__(self, scene_map):
		# sets the scene_map argument to the scene_map local variable
		# to be referred to in this class
        self.scene_map = scene_map
	
	# declares the play method.
    def play(self):
		# sets the variable 'current_scene' to the result returned
		# from the calling the opening_scene function (from the Maps class)
		# on the self.scene_map variable
        current_scene = self.scene_map.opening_scene()
		# sets the variable 'last_scene' to the result returned from calling
		# the 'next_scene' function from self.scene_map, and gives it the argument
		# 'finished'
        last_scene = self.scene_map.next_scene('finished')
		
		# as long as the current_scene value and last_scene value don't match...
        while current_scene != last_scene:
			# sets 'next_scene_name' to value received by calling the enter()
			# function on the current_scene
			next_scene_name = current_scene.enter()
			# sets current_scene to the value returned by calling 'next_scene'
			# with next_scene_name as parameter on the scene_map
			current_scene = self.scene_map.next_scene(next_scene_name)
			
		#be sure to print out the last scene
        current_scene.enter()

# sets up our 'Death' class, which is-a Scene (inherits from Scene)
class Death(Scene):
	
	#creates list, 'quips' of different phrases for when the user dies
    quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud... if she were smarter.",
		"Such a luser.",
		"I have a small puppy that's better than this."
	]
	
	# for the enter function, prints a random quip from the list
	# gets the random number by getting a randint from 0 - length of quips
	# and exits the program
    def enter(self):
        print Death.quips[ranint(0, len(self.quips)-1)]
        exit(1)


# creates the class for the first room, "Central Corridor"
# which is-a "Scene" (inherits from the Scene class)
class CentralCorridor(Scene):

	# redefines the 'enter' method (inherited from 'Scene') to print the
	# listed blocks of text.
    def enter(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew. You are the last surviving member and your last"
		print "mission is to get the neutro destruct bomb from the Weapons Armory,"
		print "put it in the bridge, and blow the ship up after getting into an "
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armory when"
		print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
		print "flowing around his hate-filled body. He's blocking the door to the"
		print "Armory and about to pull a weapon to blast you."
		
		# prompts the user for input and stores it in a var, 'action'
		action = raw_input("> ")
		
		#aaand you understand how the rest of this works. the only important thing
		# is if you choose wrong, it 'returns' 'death' as the scene name, for the map to process
		if action == "shoot!":
			print "Quick on the draw, you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim. Your laser hits his costume but misses him entirely. This"
			print "completely ruins his brand new costume his mother bought him, which"
			print "makes him fly into an insane rage and blast you repeatedly in the face until"
			print "you are dead. Then he eats you."
			return 'death'
			
		elif action == "dodge!":
			print "Like a world class boxer, you dodge, weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge, your foot slips and you"
			print "bang your head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			return 'death'
			
		elif action == "tell a joke":
			print "Lucky for you, they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
			print "The Gothon stops, tries not to laugh, and then busts out laughing and can't move."
			print "While he's laughing, you run up and shoot him square in the head"
			print "putting him down, then jump through the Weapon Armory door."
			return 'laser_weapon_armory'
		
		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'

			
# sets up a class for the Laser Weapon Armory room, which is-a Scene
# (inherits from the 'Scene' class)
class LaserWeaponArmory(Scene):
	
	# again, redefining the 'enter' method from Scene to replace it with the text
    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding. It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container. There's a keypad lock on the box"
        print "and you need the code to get the bomb out. If you get the code"
        print "wrong 10 times, then the lock closes forever and you can't"
        print "get the bomb. The code is 3 digits."
        
		# sets code to a string of 3 integers, selected randomly using randint()
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1, 9))
		# sets guess variable to user input
        guess = raw_input("[keypad]> ")
		# keeps track of the number of times the user has guessed
        guesses = 0
		
		# as long as the user hasn't guessed the code and we're still under 10 guesses
        while guess != code and guesses < 10:
			# prints 'wrong guess' sound
			print "BZZZEDDDD!"
			# adds one to guesses and prints how many guesses we've used
			guesses += 1
			print "Guesses used, out of 10: %d" % guesses
			# prompts user to guess again
			guess = raw_input("[keypad]> ")
		
		# if the user guesses it right, prints this text and returns 'the_bridge'
		# which is the next room
        if guess == code:
			print "The container clicks open and the seal breaks, letting gas out."
			print "You grab the neutron bomb and run as fast as you can to the"
			print "bridge where you must place it in the right spot."
			return 'the_bridge'
		# if we DON'T get it right within 10 guesses, then we're directed to 'death'
        else: 
			print "The lock buzzes one last time and then you hear a sickening"
			print "melting sound as the mechanism is fused together."
			print "You decide to sit there, and finally the Gothons blow up the"
			print "ship from their ship and you die."
			return 'death'
			
# you know how this one works too... nothing fancy  here	
class TheBridge(Scene):

    def enter(self):
        print "You burst onto the Bridge with the neutron destruct bomb"
        print "under your arm and surprise 5 Gothons who are trying to"
        print "take control of the ship. Each of them has an even uglier"
        print "clown costume than the last. They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."
		
        action = raw_input("> ")
		
        if action == "throw the bomb":
			print "In a panic you throw the bomb at the group of Gothons"
			print "and make a leap for the door. Right as you drop it a"
			print "Gothon shoots you right in the back killing you."
			print "As you die you see another Gothon frantically try to disarm"
			print "the bomb. You die knowing they will probably blow up when"
			print "it goes off."
			return 'death'
			
        elif action == "slowly place the bomb":
			print "You point your blaster at the bomb under your arm"
			print "and the Gothons put their hands up and start to sweat."
			print "You inch backward to the door, open it, and then carefully"
			print "place the bomb on the floor, point your blaster at it."
			print "You then jump back through the door, punch the close button"
			print "and blast the lock so the Gothons can't get out."
			print "Now that the bomb is placed, you run to the escape pod to"
			print "get off this tin can."
			return 'escape_pod'
        else:
			print "DOES NOT COMPUTE!"
			return "the_bridge"

# sets up the Escape Pod class, which is-a Scene (inherits from)			
class EscapePod(Scene):
	# overwrites the enter function from Scene, yadda yadda yadda
    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes. It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference. You get to the chamber with the escape pods, and"
        print "now need to pick one to take. Some of them could be damaged"
        print "but you don't have time to look. There's 5 pods, which one"
        print "do you take?"
		
		# assigns the 'good_pod' to be a random integer between 1 and 5
        good_pod = randint(1,5)
		# prompts the user to guess.
        guess = raw_input("[pod #]> ")
		
		# if the guess is wrong... we die.
        if int(guess) != good_pod:
			print "You  jump into pod %s and hit the eject button." % guess
			print "The pod escapes out into the void of space, then"
			print "implodes as the hull ruptures, crushing your body"
			print "into jam jelly."
			return 'death'
		# if the guess is right, we are sent to 'finished'!
        else:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod easily slides out into space heading to"
			print "the planet below. As it flies to the planet, you look"
			print "back and see your ship implode then explode like a"
			print "bright star, taking out the Gothon ship at the same"
			print "time.  You won!"
			
			return 'finished'

# sets up a specific class for "Finished," which inherits from "Scene"			
class Finished(Scene):
	
	# overwrites the 'enter' method to say we won and returns itself.
	def enter(self):
		print "You won! Good job."
		return 'finished'

# sets up our Map class, to keep track of all the rooms.
class Map(object):
	# creates a dict of the scene name along with the Instance of each room
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }
	
	# initializes with the starting scene
    def __init__(self, start_scene):
		# sets the start_scene to self.start_scene
        self.start_scene = start_scene
	
	# this is our next_scene function, used in the engine
    def next_scene(self, scene_name):
		# gets the Instance associated with the scene_name from the scenes dict
		# and sets it equal to val
        val = Map.scenes.get(scene_name)
        return val
	
	# this is our opening_scene function, used in the engine
    def opening_scene(self):
		# returns the start_scene passed ini the initialization of the class
        return self.next_scene(self.start_scene)

# creates an instance of Map, with 'central_corridor' as our start_scene argument
a_map = Map('central_corridor')
# creates an instance of the Engine, with the Map Instance we just created
a_game = Engine(a_map)
# calls the 'play' method on this instance of Engine
a_game.play()