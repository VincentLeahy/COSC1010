#
# Name Vincent Leahy
# Date 3/30/2025
# Lottery Number Generator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random

MAX_DIGITS = 7 #max number of digits
START = 0 #start of the random number range
END = 9 #End of the random number range

# main functions
def main():
	#create list
	numbers = [0] * 7

	#populate the list with random numbers.
	for index in range(MAX_DIGITS):
		numbers[index] = random.randint(START, END)

	#Display the random numbers.
	print('Here are your lottery numbers:')
	for index in range(MAX_DIGITS):
		print(numbers[index], end='')
	print()

#call the main function.
main()