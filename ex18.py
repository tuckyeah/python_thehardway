#this is like argv
#first, we tell python to make a function by saying 'def'
#then we give that function a name, 'print_two_again'
#then we tell it we want parameter *args
#then we need a colon
def print_two(*args):
#all indented lines after the 'def' become part of the function
	#unpack the arguments, just like argv
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#except we don't need that splat operator :)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#this just takes one argument	
def print_one(arg1):
	print "arg1: %r" % arg1
	
#this takes no arguments
def print_none():
	print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()