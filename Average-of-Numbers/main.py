#
# Name Vincent Leahy
# Date 3/16/2025
# Average of Numbers Programming Project
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

def main():
    numbersFile = open('numbers.txt', 'r')

    total = 0
    numberOfLines = 0
    line = numberFiles.readline()

    while line != '':
        numberOfLines += 1
        total += int(line)
        line = numbersFile.readline()

    average = total / numberOfLines

    print('The Average is', average)