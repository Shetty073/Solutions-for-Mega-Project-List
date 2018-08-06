for num in range(2,100000):
	if all(num%i!=0 for i in range(2,num)):
		print(num)
		q = input("Press 'q' and enter to quit or just press enter to get to the next prime number: ")
		if q == 'q':
			exit()
		else:
			pass
