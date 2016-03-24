from sys import exit
from random import randint
import diceroll

class Room(object):
    
    def enter(self):
	    print "This shouldn't show up ever, since this is just our base class."
	    exit(1)

    def replay(self):
        print "Would you like to play again?  y/n"
        input = raw_input("> ")
        if input == "y":
            a_map = Map('bedroom')
            a_game = Engine(a_map)
            a_game.play()
        elif input == "n":
            print "Goodbye!"
            exit(1)	
        else: 
            print "Please print a value I understand."
            self.replay()

			
class Engine(object):

    def __init__(self, room_map):
        self.room_map = room_map

    def play(self):
        current_room = self.room_map.opening_room()
        last_room = self.room_map.next_room('finished')

        while current_room != last_room:
            next_room_name = current_room.enter()
            current_room = self.room_map.next_room(next_room_name)

        current_room.enter()


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
        guesses = 0
        
        print "You find yourself in what appears to be an indoor garden of some sort... You are surrounded by"
        print "decorative trees and flowers. There is a bridge over a small koi pond, and on the other side"
        print "there is a door. Next to the door is a keypad. It seems to be asking for a code..."
        print "You stand atop the bridge and look down into the koi pond. You count %d fish..." % self.koi

        while True:
            
            answer = raw_input("> ")

            if answer == "pond":
                print "You stand atop the bridge and look down into the koi pond. You count %d fish..." % self.koi

            elif answer == "trees":
                print "What beautiful tall trees... though you notice they seem to be concealing the sky."

            elif answer == "flowers":
                print "Such beautiful flowers, they smell so nice... though no clues here!"

            elif answer == "door":
                print "The door needs a code!"
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
                    self.replay()
            
            else:
                print "Please enter a value I understand."
    

class Library(Room):

    def __init__(self):
        self.books = ["Apples to Apples", "Bananas and You", "Cranberry Delights", 
                      "Donuts to Donuts", "Eggs Five Ways", "Fun with Flan"]  
        self.right_book = self.books[randint(0, len(self.books)-1)]
        self.following_room = 'basement'
    
    def enter(self):
        print "You find yourself in a room, surrounded by shelves full of books."
        print "There is no door in sight, but there is a collection of books in front of you"
        print "that looks strangely different than the others. You ready the titles..."
        print "(the correct book is: %s)" % self.right_book

        for i in self.books:
            print "- %s" % i 

        print "Which book do you select?"
        ans = raw_input("[book title]> ")

        while ans != self.right_book:
            print "Nothing happens..."
            ans = raw_input("[book title]> ")

        if ans == self.right_book:
            print "A door slides open!"
            return 'basement'


class Basement(Room):
#add like a dictionary of puzzles? that can be randomized?

    def enter(self):
        print "You descend a dark and narrow spiral stone staircase that leads deep into"
        print "the basement of the house... Finally, you reach an empty chamber with a door"
        print "at the other end. You rush towards it, but before you can reach it, an enormous"
        print "turtle appears in front of you!"
        print "'You are almost free, but before I can let you escape, you must prove you are"
        print "wise enough to make it in the real world. You have three guesses to answer my riddle.'"
        print "'What is the only thing you can add to a bucket to make it lighter?'"

        ans = raw_input("[answer]> ")
        guesses = 0

        while ans != "a hole" and guesses < 3:
            print "'Nope... You have %d guesses left.'" % (3-guesses)
            guesses += 1
            ans = raw_input("[answer]> ")

        if ans == "a hole" and guesses < 3:
            print "'Congratulations! You may pass...'"
            print "The turtle fades away, and the door opens..."
            return 'ornate_room'
        
        else:
            print "'I'm sorry... I can't let you go on, in good conscience. You must stay here.'"
            self.replay()


class OrnateRoom(Room):

    def enter(self):
        print "You find yourself in another room... and here you thought you were free!"
        print "The room is beautifully ornate, covered in gold and jewels. In the middle,"
        print "two die sit on a raised pedestal. You have 5 chances to roll doubles and escape"
        print "forever. Type 'r' to roll. Ready?"
        guesses = 0
        doubles = False
        
        while not doubles:
            ans = raw_input("[r/e]> ")
		
            if ans == "r" and guesses < 5:
                print "Number of guesses: %d" % guesses
                doubles = diceroll.roll_dice(self)
                guesses += 1

            elif guesses >= 5:
                print "No dice (haha!) You are trapped here forever!!"
                self.replay()

            else:
                print "Please print a value I understand"
                ans = raw_input("[r/e]> ")

        if doubles:
		    return 'finished'


class Finished(Room):

    def enter(self):
        print "Congratulations! You've won!"
        return self.replay()

		
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
		
a_map = Map('ornate_room')
a_game = Engine(a_map)
a_game.play()
