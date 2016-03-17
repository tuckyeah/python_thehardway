#a script to open and read the file we edited in ex16.py
from sys import argv

script, filename = argv

target = open(filename)

print "Here's what the file %r says now:" % filename
print target.read()

target.close()