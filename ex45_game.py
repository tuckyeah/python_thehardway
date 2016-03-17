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
	
    def enter(self):
        print "You wake up, confused, in a strange bedroom of sorts. There is"
        print "not much by way of furniture - only a plain desk and chair, the bed"
        print "you are currently lying on, and a door. What would you like to investigate first?"

        answer = raw_input("> ")
        key = False
		
        while not key:
            if answer == "bed":
		        print "A thin mattress on a metal frame. Not particularly comfortable, "
		        print "and not particularly interesting either."
		        answer = raw_input("> ")
            elif answer == "door":
				print "No luck - the door is locked. You're not escaping that easy!"
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

    def enter(self):
	    pass
		

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

test = Bedroom()
test.enter()