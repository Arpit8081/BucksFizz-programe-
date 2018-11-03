for a in range (101):
	if (a % 3 == 0 and a % 5 == 0):
		print("BucksFizz")
	elif (a % 3 == 0):
		print("Buck")
	elif (a % 5 == 0):
		print("Fizz")
	else:
		print (a)	
	