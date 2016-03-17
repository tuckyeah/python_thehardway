## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## class Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## has-a attribute 'name'
		self.name = name
		
## class Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## has-a attribute 'name'
		self.name = name
		
## class Person is-a object
class Person(object):

	def __init__(self, name):
		## has-a attribute 'name'
		self.name = name
		
		## Person has-a pet of some kind
		self-pet = None
		
## class Employee is-a Person
class Employee(Person):

	def__init__(self, name, salary):
		## ?? What is this strange magic??
		super(Employee, self).__init__(name)
		## Employee has-a attribute 'salary'
		self.salary = salary
		
## class Fish is-a object
class Fish(object):
	pass
	
## class Salmon is-a Fish
class Salmon(Fish):
	pass
	
## class Halibut is-a Fish
class Halibut(Fish):
	pass
	
## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet
## pet is-a Cat
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

##frank has-a pet
frank.pet = rover

##flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
