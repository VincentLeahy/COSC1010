#
# Name: Vincent Leahy
# Date 2/23/2025
# Kilometer Converter Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

CONVERSION_FACTOR = 0.6214

def main():
	while True: #preventing the loop
		try:
			#Get the distance in kilometers.
			kilometers = float(input("Enter a distacne in kilometers: "))
			break #if input is valid break out of the loop
		except ValueError:
			print("Please enter a valid number.")
	
	#Display the distane converted to miles.
	show_miles(kilometers)

def show_miles(km):
	#Calculate miles.
	miles = km * CONVERSION_FACTOR
	
	#display the miles
	print(km, 'kilometers equals', miles, 'miles.')

main()