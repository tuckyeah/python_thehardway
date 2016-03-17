#sets variable 'formatter' to a string that is just 4 %r formatters
formatter = "%r %r %r %r"

#for comparison, a variable with 4 %s formatters
formatter_s = "%s %s %s %s"

#prints formatter variable string, with integers 
#returns in the exact same format seen here
print formatter % (1, 2, 3, 4)

#prints formatter variable string, with given strings in order
#returns with single quotes around each string (as opposed to just double quotes around the entire thing)
print formatter % ("one", "two", "three", "four")

#for comparison, returns just a string with no quotes
print formatter_s % ("one", "two", "three", "four")

#prints formatter variable string, with boolean values given
#returns exactly the same format seen here
print formatter % (True, False, False, True)

#prints formatter variable string, with itself as the given values
#prints '%r %r %r %r' (in single quotes) four times
print formatter % (formatter, formatter, formatter, formatter)

#priints formatter variable string, with the given string sentences
#returns them in one line with single quotes around each, 
#EXCEPT for line 32, which is returns in double quotes (????)
print formatter % (
	"I had this thing.",
	"That you could up right.",
	"But it didn't sing.",
	"So I said goodnight."
)