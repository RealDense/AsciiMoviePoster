
numbers = [1,2,3,4,5]

#while numbers:
for I in range(6):
	t = numbers.pop(0)
	print t
	print numbers
	if not numbers:
		break
		print "nothing"
	print "more nothings"
	#del numbers[1:]
