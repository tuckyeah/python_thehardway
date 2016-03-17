from sys import argv

script, first, second, third = argv
#when we run this in the command line, we _must_ include
# 3 variables on the command line. so for instance:
# $ python ex13.py first, 2nd, 3rd
# Rememebr: The script NAME counts as an argument here!!!

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
something = raw_input("type something here ")
print something

#argv works when we want the user to input something 
	#on the command line / before the scrip runs

#raw_input when we want them to input something 
	#when the script is already running