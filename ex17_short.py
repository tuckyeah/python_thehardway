from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)
print "Does the output file exist? %r" % exists(to_file)

out_file = open(to_file, 'w').write(indata)

print "Alright, all done."

### if we want to be really fancy...

#	indata = open(from_file).read(); out_file = open(to_file, 'w').write(indata)