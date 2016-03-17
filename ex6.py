# sets variable 'x' equal to the string, and 
# uses the %d formatter to include the number 10
x = "There are %d types of people." % 10
#sets variable 'binary' to string
binary = "binary"
#sets variable 'do_not' to string
do_not = "don't"
#sets y to string sentence and includes formatters 
# %s to insert strings associated with variables 'binary' and 'do_not'
y = "Those who know %s and those who %s."  % (binary, do_not)

#prints x, thereby printing string associated with x
print x
#same as above, but with y 
print y

#printing additional string in addition to x, which is included
# in string with %r as the formatter
print "I said: %r." % x
#printing y in the same manner as above, but using %s as the formatter
print "I also said:'%s'." % y

# %r automatically includes '' around x when it prints, while
# %s does not automatically includes the ''.

#sets variable 'hilarious' to boolean value 'False'
hilarious = False
#sets 'joke_evaluation' variable to string with %r formatter included, 
# though not specified here.
joke_evaluation = "Isn't that joke so funny?! %r"

#prints string associated with variable 'joke_evaluation'
# and sets value of variable 'hilarious' as the %r formatter value
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#concatenates strings associated with variable w and e into one string
print w + e 