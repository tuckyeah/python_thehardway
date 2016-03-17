#gets the argument variable module from the sys package
from sys import argv

#argv will be set to the script and file name, which we must enter on the command line
# eg $ python ex16.py test.txt
# so then - 'script' = ex16.py; 'filename' = test.txt
script, filename = argv

print "We're going to erase %r." % filename
#not totally sure what ctrl-c does.. it does exit the script though, 
#as well as throwing an EOFError
print "If you don't want that, hit CTRL-C (^C)"
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
#sets variable 'target' equal to the file object returned from 'open'
#'open' takes the filename parameter, from argv, which we set in the command line
# 'w' stands for 'write' and truncates the file (if it already exists)
target = open(filename, 'w')

#truncates (deletes) all content in the file.
#this step technically isn't necesssary, 
#since the 'w' in our open() call theoretically truncates the file
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
#prompts the user three times for input, and sets it to variables
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
#writes each of those lines to 'target', the file object
#with a new line between each of them
#PAY ATTENTION TO THE PARENTHESIS HERE!!!
target.write("%s \n%s \n%s \n" % (line1,line2,line3))

print "And finally, we close it."
target.close()