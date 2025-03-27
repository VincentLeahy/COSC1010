#
# Name Vincent Leahy
# Date 3/16/2025
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Open the file.

def main():
    # Open the file for reading.
    myfile = open('numbers.txt', 'r')

    total = 0
    numberOfLines = 0

    # Reading the file line by line. 
    for line in myfile:
        numberOfLines += 1
        total += int(line)

    # Calculating the average of the numbers inside the file.
    if numberOfLines > 0:
        average = total / numberOfLines
        print('The average is', average)
    else:
        print('No numbers to calculate an average.')

    # Close the file after processing
    myfile.close() 

main()