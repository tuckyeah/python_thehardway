# INHERITANCE
class Parent(object):
	
	def override(self):
	#this function will be overridden in the Child class
		print "PARENT override()"
		
	def implicit(self):
	# implicit function is not defined in the Child class, so this will print the same either way
		print "PARENT implicit()"

	def altered(self):
	#implicit-ish function, since Child calls back to it but does not change it
		print "PARENT altered()"

class Child(Parent):
	
	def override(self):
		print "CHILD override()"
		
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"
	
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

print '-' * 10

#COMPOSITION
class Other(object):

	def override(self):
		print "OTHER override()"
		
	def implicit(self):
		print "OTHER implicit()"
		
	def altered(self):
		print "OTHER altered()"
		
class Child(object):

	def __init__(self):
		self.other = Other()
		
	def implicit(self):
		self.other.implicit()
		
	def override(self):
		print "CHILD override()"
		
	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		self.other.altered()
		print "CHILD, AFTER OTHER altered()"
		

son = Child()

son.implicit()
son.override()
son.altered()