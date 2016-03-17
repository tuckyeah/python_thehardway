#defines a function called 'add' that takes 2 arguments
#RETURNS the result of adding those two arguments
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

#defines a function called 'subtract' that takes 2 arguments
#RETURNS the result of subtracting a from b	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b 

#defines function called 'multiply' that takes 2 arguments
#RETURNS the result of multiplying a and b
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b 

#defines a function called 'divide' that takes 2 arguments
#RETURNS the result of dividing a by b 
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b 
	

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


#this is an extra credit puzzle
print "Here is a puzzle."
#this translates to...74-180*(50/2)+35
#or... d + b * (a / 2) - c
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

print "---"

#24 + 34.0 / 100.0 - 1023.0 should be our next test
who = subtract(1023.0, add(24.0, divide(100.0, 34.0)))
print who