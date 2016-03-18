from sys import exit
from random import randint

class Room(object):

    def enter(self):
	    print "This shouldn't show up ever, since this is just our base class."
	    exit(1)


class Engine(object):

    def __init__(self, room_map):
	    self.room_map = room_map

    def play(self):
        user = Player()

		
class Player(object):

    def __init__(self):
		self.inventory = []
		
    def add_inventory(self, item):
	    self.inventory.append(item)
		
    def list_inventory(self):
        for i in inventory:
            print "%s" % i


class Bedroom(Room):
	#remember to add in a return here!
    def enter(self):
        print "You wake up, confused, in a strange bedroom of sorts. There is"
        print "not much by way of furniture - only a plain desk and chair, the bed"
        print "you are currently lying on, and a door. What would you like to investigate first?"

        answer = raw_input("> ")
        key = False
		
        while not key:
            if answer == "bed":
		        print "A thin mattress on a metal frame. Not particularly comfortable, "
		        print "and not particularly interesting either.\n"
		        answer = raw_input("> ")
            elif answer == "door":
				print "No luck - the door is locked. You're not escaping that easy!\n"
				answer = raw_input("> ")
            elif answer == "desk":
		        print "A boring wooden desk, just like the kind you had in school..."
		        print "Although on closer investigation, you notice a small button"
		        print "on the underside. You press it and a secret drawer opens!"
		        print "There is a key inside! You take the key."
		        print "\n"
		        key = True
            else: 
		        print "I don't understand. Please enter a value I understand."
		        answer = raw_input("> ")

        if key:
            print "Key in hand, you head to the door. Sure enough, the key fits in the lock,"
            print "you turn the handle and open the door..."
            return 'koi_pond'
        else: 
            print "This should never appear either."

			
class KoiPond(Room):
    def __init__(self):
        self.koi = randint(1, 9)
		
    def enter(self):
        print "You find yourself in what appears to be an indoor garden of some sort... You are surrounded by"
        print "decorative trees and flowers. There is a bridge over a small koi pond, and on the other side"
        print "there is a door. Next to the door is a keypad. It seems to be asking for a code..."
        self.explore()
		
    def explore(self):
        while True:
            answer = raw_input("> ")
            if answer == "pond":
                print "You stand atop the bridge and look down into the koi pond. You count %d fish..." % self.koi
            elif answer == "trees":
                print "What beautiful tall trees... though you notice they seem to be concealing the sky."
            elif answer == "flowers":
                print "Such beautiful flowers, they smell so nice... though no clues here!"
            elif answer == "door":
                print "The door needs a code! Do you want to enter a number? y/n"
                enter_code = raw_input("> ")
                if enter_code == "n":
                    print "Where to?"
                    self.explore()
                elif enter_code == "y":
                    self.keypad()
                else:
                    print "please type 'y' or 'n'"
            else:
                print "Please enter a value I understand."
    
    def keypad(self):
        guesses = 0
        code = raw_input("[keypad]> ")
        
        while int(code) != self.koi and guesses < 5:
            print "Wrong! Guess again!"
            code = raw_input("[keypad]> ")
            guesses += 1

        if int(code) == self.koi:
            print "You did it! The door unlocks."
			return 'library'
        else: 
            print "Oh no! Too many guesses :( You are trapped here forever!"

			
class Library(Room):

    def enter(self):
	    pass
		

class Basement(Room):

    def enter(self):
	    pass
		
		
class OrnateRoom(Room):

    def enter(self):
	    pass

class Finished(Room):

    def enter(self):
	    pass
		
    def replay(self):
	    pass
		
class Map(object):
	# create a dictionary of the rooms
	# then create a list of their keys
	# pick a random room, pop it (so it's not in the array) and return it
    rooms = {
        'bedroom': Bedroom(),
        'koi_pond': KoiPond(),
        'library': Library(),
        'basement': Basement(),
        'ornate_room': OrnateRoom()
    }

    def __init__(self, start_room):
        pass
		
    def next_room(self, room_name):
	    pass 
		
    def opening_room(self):
	    pass 
		
a_map = Map('bedroom')
a_game = Engine(a_map)
a_game.play()

test = KoiPond()
test.enter()