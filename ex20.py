#imports 'argv' module from sys package
from sys import argv

#unpacks argv into 'script' and 'input_file' variables
#which were passed to it on the command line :)
script, input_file = argv

#defines a function called 'print_all,' which will print all the data from the file
#it takes one argument, f (which may or may not be significant/convention)
def print_all(f):
	#prints the data from the file, f.
	print f.read()

#defins a function called 'rewind,' which will bring us back to the start
#it takes one argument, f. 
def rewind(f):
	#calls 'seek()' on the file, and tells it to go to line 0
	# so the start of the file
	f.seek(0)

#defines a function called 'print_a_line', which will print one line at a time
#takes two arguments, line_count and f.	
def print_a_line(line_count, f):
	#prints the current line number, followed by the contents of that line
	#the comma keeps us from having a double space at the end of each line, from readline()
	print line_count, f.readline(),
	
#open the file we listed at the beginning
#and sets the file object to variable 'current_file'
current_file = open(input_file)

print "First let's print the whole file:\n"
#calls 'print_all' function on the current_file object.
#this prints all the contents in the current file.
print_all(current_file)

print "Now let's rewind, kind of like a tape."
#calls the rewind function on our current_file
#so it 'seeks' back to the first line
rewind(current_file)

print "Let's print three lines:"

#sets variable 'current_line' to 1
#current_line represents the line_count needed for our print_a_line function
current_line = 1
#calls print_a_line with the current_line variable (1) and the current_file variable
#this prints the first line of the file.
print_a_line(current_line, current_file)

#increment the current_line variable, so it becomes '2'
#thereby moving to the next line
current_line += 1
#call the print_a_line function again, with our updated current_line
print_a_line(current_line, current_file)

#and again, incrementing to become 3, so now we're on line 3
current_line += 1
#and prints the final line 
print_a_line(current_line, current_file)