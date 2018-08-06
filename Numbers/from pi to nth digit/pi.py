from math import pi

def pi_dec(n):
	if n > 15 or n < 1:
		print("\nPlease provide a valid number in range of 1 to 15...")
	else:
		print(f"PI = {str(pi)[0:n+2]}")

pi_dec(n=int(input("\nUp to how many decimal places do you want the value of 'pi'? \n> ")))
