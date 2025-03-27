#
# Name Vincent Leahy
# Date 3/16/2025
# File Display Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Open the file.

myfile = open('numbers.txt', 'r')

# Read and display the files contents.
for line in myfile:
    number = int(line)
    print(number)

# Close File
myfile.close()
