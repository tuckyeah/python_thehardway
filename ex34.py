#imports 'exit' module from sys library
from sys import exit

#defines a function called 'gold room',  that takes no args
def gold_room():
	print "This room is full of gold.  How much do you take?"
	
	#asks the reader to input a number
	choice = raw_input("> ")
	#checks to see if the number includes a 0 or 1 (which is a stupid, stupid way of doing this)
	#if so, converts the choice to an int and sets it to 'how_much'
	#if we want to get fancy, we can do choice.isdigit()
	try:
		how_much = int(choice)
	#otherwise, chastises us and ends the program
	except:
		dead("Man, learn to type a number.")
	
	#if the number chosen is less than fifty, gives the message and ends the program.
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	#if it's greater than 50, sends us to the 'dead' function
	#and passes an argument with the reason why
	else:
		dead("You greedy bastard!")

#defines a function called 'bear room' that takes no args
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	#sets variable 'bear_moved' to False
	bear_moved = False
	
	#starts a while-loop set to True, making it an infinite loop
	#meaning it will keep prompting the user for answers until we end this function
	while True:
		choice = raw_input("> ")
		
		#if the user takes the honey, sends them to the dead function
		#and passes an argument with the reason why
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		#if the user chooses 'taunt' bear AND the bear is still in front of the door 
		#which we check by saying "not bear_moved," meaning it's checking to see if it's false
		#the bear moves from the door, and we set bear_moved to true
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		#if the user tries to taunt the bear after the bear has moved,
		#it sends us to dead function the string arg as to why
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		#if the bear has moved from the door (been set to true)
		#then we can open the door, and it sends us to the goldroom function
		elif choice == "open door" and bear_moved:
			gold_room()
		#if the user inputs something else, it prompts an msg telling them we don't understand
		else:
			print "I got no idea what that means."

#defines a function called 'cthulhu room' that takes no args
def cthulhu_room():
	#the statements give the reader choices, and then prompts input
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	choice = raw_input("> ")
	
	#if the word 'flee' is in the response, it sends us back to the start function
	if "flee" in choice:
		start()
	#if the word 'head' is in the response, it sends us to 'dead' with a string arg saying why
	elif "head" in choice:
		dead("Well that was tasty!")
	#otherwise, it prompts the function to start over again
	else:
		cthulhu_room()

#defines our dead function, taking one argument, a string that says why
def dead(why):
	print why, "Good job!"
	exit()

#defines the start function, which gives our initial choices
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
	
#calls the start function at the end of the script to start the game!
start()