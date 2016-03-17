i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers :"

for num in numbers:
	print num
	
# converting the while loop to a function
def while_loop(start, end, increment):
	while start < end:
		print "Adding %d to list" % start
		numbers.append(start)
		start += increment

while_loop(0, 20, 5)

#converting to for-loop

def for_loop(start, end):
	for i in range(start, end):
		numbers.append(i)
		start += 2
		print numbers

for_loop(2, 12)
