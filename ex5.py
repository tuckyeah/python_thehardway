name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
cm_height = height * 2.54
weight = 180.0 # lbs
kg_weight = weight * 0.453
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "In centimeters, that's %i cm" %cm_height
print "He's %d pounds heavy." % weight
print "In kilograms, that's %i kg" % kg_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)