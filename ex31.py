print "You enter a dark room with three doors. Which door do you choose?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear
		
elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
	print "You have entered the matrix. You are now surrounded by glittering strings of code. In your hand, a red pill and a blue pill. Which do you take?"
	
	pill = raw_input("> ")
	
	if pill == "red":
		print "You took the red pill and went further into the matrix. Now you're a cyborg. Great work!"
	elif pill == "blue":
		print "You take the blue pill and go back home. Fair choice."
	else:
		print "You take neither and disappear completely, fading into the void."
else:
	print "You stumble around and fall on a knife and die. Good job!"
