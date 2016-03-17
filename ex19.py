#defines a function called "cheese_and_crackers"
#it takes two arguments, cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#prints the cheese_count variable
	print "You have %d cheeses!" % cheese_count
	#prints the boxes_of_crackers variable
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man, that's enough for a party!"
	print "Get a blanket.\n"


print "We can just give the function numbers directly:"
#puts the number 20 as 'cheese_count' and 30 as 'boxes_of_crackers'
cheese_and_crackers(20, 30)


print "OR, we can use the variables from our script:"
#sets variable for amount of cheese and amount of crackers
amount_of_cheese = 10
amount_of_crackers = 50

#passes these newly set variables to the function in order
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
#adds 10+20 in the cheese_count place and 5 + 6 in the boxes_of_crackers place
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
#adds 100 to the number in our amount_of_cheese variable
#and 1000 to the number in our amount_of_crackers variable
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) 

print "----"

#defines a function called "how_old"
#it takes two arguments, birth_year and current_year
def how_old(birth_year, current_year):
	#sets temp variable 'age' to be the value passed in for current_year minus the value for birth_year
	#both arguments have int() before them to make sure they are treated as integers
	age = int(current_year) - int(birth_year)
	#returns a string with the calculated age
	print "You are %d years old!" % age
	
print "My age: "
how_old(1988, 2016)

print "Liz's age in 2020: "
how_old(1987, 2020)

print "How long since columbus landed in america:"
how_old(1492, 2016)


print "Now let's try with some questions."
#asks the user for the year they were born, and sets it to variable 'year_born'
year_born = raw_input("What year were you born? ")
#asks user for current year, and sets it to variable 'this_year'
this_year = raw_input("What year is it? ")

#calls the 'how_old' function with the answers we just got from the user
#in the form of the variables those answers were assigned to
how_old(year_born, this_year)