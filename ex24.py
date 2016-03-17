print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "------------"
print poem
print "------------" 


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

#defines a function called 'secret_formula' that takes one argument, 'started'
def secret_formula(started):
	#assigns temp variable 'jelly_beans' to value in arg 'start' multiplied by 500
	jelly_beans = started * 500
	#now that we have jelly_beans, we'll set 'jars' equal to jelly_beans divided by 100
	jars = jelly_beans / 1000
	#and we'll set crates equal to jars divided by 100
	crates = jars / 100
	return jelly_beans, jars, crates
	
#sets a variable, 'start_point', that we then pass to the function
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

#updates 'start_point' to be itself divided by 10
start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)