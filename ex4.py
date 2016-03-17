#VARIABLES
#sets number of cars
cars = 100
#sets space in each car
space_in_a_car = 4.0
#sets number of drivers
drivers = 30
#sets number of passengers
passengers = 90
#the cars not driven are the number of cars minus number of drivers
cars_not_driven = cars - drivers
#sets the number of driven cars to the number of available drivers
cars_driven = drivers
#sets carpool capacity to the number of cars driven times the amount of space in each car
carpool_capacity = cars_driven * space_in_a_car
#sets average passengers to the number of passengers, divided by the number of cars driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available"
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."