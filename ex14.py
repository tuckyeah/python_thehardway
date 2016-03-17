from sys import argv

#remember, we have to put the arguments on the command line!!

script, user_name = argv
#setting the prompt value here lets us change it later on
prompt = '>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
#prompts the user for an answer and sets it to variable "likes"
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
#prompts the user for input and sets it to variable 'lives'
lives = raw_input(prompt)

print "What kind of computer do you have?"
#prompts user for input and sets it to variable 'computer'
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice. 
""" % (likes, lives, computer)