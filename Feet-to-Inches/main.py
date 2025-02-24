#
# Name: Vincent Leahy
# Date: 2/23/2025
# Feet to Inches Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.


# Constant for the number of inches per foot
INCHES_PER_FOOT = 12

# main function
def main():
	while True:
		try:
			# Get a number of feet from the user.
			feet = int(input("Enter a number of feet: "))
			break #if input is valid, break out of loop
		except ValueError:
			print("Please enter a valid number.")
	#Convert that to inches
	print(feet, "equals", feet_to_inches(feet), "inches.")
#The Feet_to_inches converts feet to inches 
def feet_to_inches(feet):
	return feet * INCHES_PER_FOOT
#Call the main function.
main()