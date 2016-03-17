from sys import argv
#import 'exists' module from 'os.path'
#exists module checks if file exists, based on string name passed as argument
#returns boolean - True if yes, False if not.
from os.path import exists

#takes script name (ex17.py), file to copy from and file to copy to
script, from_file, to_file = argv

#confirms we know which files we're copying from/to
print "Copying from %s to %s" % (from_file, to_file)

#sets 'indata' to open the copyfromfile and then calls read on it
indata = open(from_file).read()

#gets length of string passed to it,
#which is the read data from the copyfrom file
print "The input file is %d bytes long" % len(indata)

#checks to make sure a file named whatever to file we made exists
#if it doesn't exist, it doesn't matter - it will make that file
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort"
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()



