#import argument variable from python sys
from sys import argv

#requiring 2 variables on the commandline - 
# name of executed script (ex15.py in this case) and 
# name of the file we'll be opening
# so the command line will read '$python ex15.py ex15_sample.txt'
script, filename = argv

#sets variable 'txt' to file object returned from open() call
#open() is taking the filename variable we set in argv 
txt = open(filename)
#open() opens a file using the file type, and returns a file object.
# this is the preferred way of opening a file

#prints file name
print "Here's your file %r:" % filename
#we call the read() function on txt (the file object)
#which reads and then prints the content
print txt.read()

#always remember to close open files when we're done 
#there's an upper limit to numbero f open files we can have at a time
# and they stand the risk of corruption/data loss
txt.close()

#and repeat
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()