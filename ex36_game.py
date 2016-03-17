from sys import exit

#UPKEEP (replay, start, dead)

def replay():
#asks if the user if they'd like to play again
#if yes, sends them back to start()
#if no, prints "Goodbye" and exits the program
#otherwise, prompts the user to try again 
	print "Would you like to restart? y/n"
	
	choice = raw_input("> ")
	
	if choice == "y":
		start()
	elif choice == "n":
		print "Goodbye!" 
		exit(0)
	else:
		print "I don't understand."
		replay()

def start():
#start of the game function
#asks the user if they want to go into the blue or red door
#or prompts the user to try again
	print "You are in a dark room, and two doors stand before you."
	print "One is red and one is blue. Which do you choose?"
	
	choice = raw_input("> ")
	
	if "red" in choice:
		print "You go into the red door..."
		red_room()
	elif "blue" in choice:
		print "You go into the blue door..."
		blue_room()
	else:
		print "Enter a value I understand, please."

def dead(why):
#if the user dies, this is the function that is called. 
#it takes one argument, a string with the reason why, and prints that + the dead message
#then promtps the user if they want to replay
	print why, "And so you die. Bummer."
	replay()


"""
ROOMS

blue room (troll (fight, flirt, pay)) -> purple room (naked emperor) -> white room
red room (riddle (wrongx3, right)) -> pink room(flowers)-> white room
"""

def blue_room():
	print "\nThere is a troll in front of you, blocking the next door."
	print "'I am tired of being alone. Pay me so I can buy a friend!' he demands. 'Or beat me in combat!'"
	print "What do you do?"
	
	choice = raw_input("> ")
	
	if "fight" in choice:
		print "Wrong choice."
		dead("The troll beats you and your puny body handily.")
	elif "flirt" in choice or "friend" in choice:
		print "The troll blushes, thrilled with human contact, and lets you pass."
		purple_room()
	elif "pay" in choice:
		print "'Pay me handsomely,' the troll demands. 'Or face the consequences.'"
		
		while True:
			payment = raw_input("How much do you pay him? > ")
			if int(payment) <= 50:
				print "Cheapskate."
				dead("The troll crushes you with an enormous fist.")
			elif int(payment) > 50:
				print "The troll seems satisfied, and lets you pass."
				purple_room()
			else:
				print "Please print a number I understand"
	else:
		print "Please enter a value I understand."
		blue_room()

		
def red_room():
# you have three chances, so guesses = 3
# while guesses < 3, it'll prompt you for your answer
# if you get it right, then
	print "\nA giant turtle is blocking your way forward. When he sees you approach, he speaks:"
	print "'Answer my riddle and you can proceed. You have three chances.'"
	print "'What's the only thing you can put in a full barrel to make it lighter?'"	

	guesses = 0
	
	while guesses < 3:
		answer = raw_input("> ")
		if "hole" in answer:
			print "'You've chosen wisely. Proceed.'"
			pink_room()
		else:
			print "Try again"
			guesses+=1
	
	dead("'This riddle too tough for you?' A hole in the floor opens and you fall through.")
		

def purple_room():
#purple room - there is a naked emperor. prompts the user to either compliment him or ignore him
#if compliment, the user can continue to the white room; otherwise, to death.
	print "\nYou enter the room and are shocked that it's full of people!"
	print "In the center of the crowd stands a naked man in a crown."
	print "'Don't my new clothes look great?' he exclaims, everyone cheers."
	print "He points at you. 'You there! What do you think of my outfit?'"
	print "What do you say? Do you tell him he's naked?"
	
	choice = raw_input("> ")
	
	if choice == "yes":
		dead("The emperor does not like being told the truth. 'Off with your head!'")
	if choice == "no":
		print "The Emperor seems pleased with your compliments, and lets you pass through."
		white_room()


def pink_room():
#pink room - it is full of flowers. asks the user if they pick one
#if they do, to death. if not, they can continue to the white room.
	print "\nYou enter a room that is FILLED with the most beautiful flowers you've ever seen."
	print "What a nice aroma..."
	print "Do you stop and pick a flower, or keep walking through to the door on the other side?"
	
	choice = raw_input("> ")
	
	if "flower" in choice:
		print "The flowers turn to ash in your hands and the room is cast into darkness."
		print "You hear something breathing behind you..."
		dead("This is one time when it doesn't pay to stop and smell the flowers!")
	if "walk" in choice:
		print "You ignore all the flowers and head straight through to the white door on the other side."
		white_room()


def white_room():
#white room - final room. asks the user if they choose riches or escape
#if riches, death. if escape, then they win!
	print "Before you stands two doorways."
	print "The one on the right is full of treasure."
	print "The one on the left is an exit to the outside."
	print "Which do you choose?"
	
	choice = raw_input("> ")
	
	if choice == "right" or "treasure" in choice:
		print "As soon as you cross the threshold, the treasure turns to dirt."
		print "The door closes behind you, and a menacing laugh echoes through the cave."
		dead("'Greed is a mortal sin, my child, so say goodbye to mortality.'")
	elif choice == "left" or "leave" in choice:
		print "Ah, fresh air! You are free at last!"
		print "Congrats, you've won!"
		replay()
	else:
		print "I don't understand. Try again."
		white_room()

start()