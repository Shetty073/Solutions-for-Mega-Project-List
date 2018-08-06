from math import e

def pi_dec(n):
	if n > 15 or n < 1:
		print("\nPlease provide a valid number in range of 1 to 15...")
	else:
		print(f"E = {str(e)[0:n+2]}")

pi_dec(n=int(input("\nUp to how many decimal places do you want the value of 'e'? \n> ")))