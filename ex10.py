tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t *Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "---"

print "this is how r works with escapes: %r" % "\nI bet it won't\nrecognize these characters"

print '''
there is no difference between triple single quotes
and triple double quotes
it's all about ~*~style~*~
'''

#does a little spinny line, but also doesn't stop lol
#while True:
#	for i in ["/","-","\\","|"]:
#		print "%s\r" % i,
		