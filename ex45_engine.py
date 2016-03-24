from sys import exit
from random import randint

class Room(object):
    def __init__(self):
		self.following_room = 'bedroom'
	
    
	def enter(self):
	    print "This shouldn't show up ever, since this is just our base class."
	    exit(1)

    def replay(self):
	    pass

class Engine(object):

    def __init__(self, room_map):
        self.room_map = room_map

    def play(self):
        current_room = self.room_map.opening_room()
        last_room = self.room_map.next_room('finished')

        while current_room != last_room:
            next_room_name = current_room.following_room
            current_room = self.room_map.next_room(next_room_name)

        current_room.enter()

class Map(object):
	# create a dictionary of the rooms
	# then create a list of their keys
	# pick a random room, pop it (so it's not in the array) and return it
    rooms = {
        'bedroom': Bedroom(),
        'koi_pond': KoiPond(),
        'library': Library(),
        'basement': Basement(),
        'ornate_room': OrnateRoom(),
        'finished': Finished()
    }

    def __init__(self, start_room):
        self.start_room = start_room
		
    def next_room(self, room_name):
        val = Map.rooms.get(room_name)
        return val
		
    def opening_room(self):
        return self.next_room(self.start_room) 
		
a_map = Map('bedroom')
a_game = Engine(a_map)
a_game.play()