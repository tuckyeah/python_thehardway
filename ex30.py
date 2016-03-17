people = 30
cars = 40
trucks = 15

#if the number of cars is greater than the number of people, 
#print "We should take cars"
if cars > people:
	print "We should take the cars."
#Else, if the number of cars is less than the number of people
#print "We should not take the cars."
elif cars < people:
	print "We should not take the cars."\
#else, if neither of the above are true, print "We can't decide"
else:
	print "We can't decide."

#if the number of trucks is greater than the number of cars
#print "That's too many trucks"	
if trucks > cars:
	print "That's too many trucks."
#Else, if the number of trucks is less than the number of cars
#print "Maybe we could take the trucks"
elif trucks < cars:
	print "Maybe we could take the trucks."
#else, if neither of the above are true, print "We still can't decide"
else: 
	print "We still can't decide."

#if the number of people is greater than the number of trucks
#print "Alright, let's just take the trucks."
if people > trucks:
	print "Alright, let's just take the trucks."
#else, if the above is false, then print "We'll just stay home."
else: 
	print "Fine, let's stay home then."