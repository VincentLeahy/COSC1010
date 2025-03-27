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
    #Opening the file and running a IOError to handle any errors that arise and if no error reading the file itself. 
    try:
        myfile = open('numbers.txt', 'r')
    except IOError as errorGenerated:
        print('File not Found:', errorGenerated)
    else:
        total = 0
        numberOfLines = 0
        line = myfile.readline()

        while line != '':
            numberOfLines += 1

             #adding number of total lines then next line reading next line.
            total += int(line)
            line = myfile.readline()

#Calculate the average
        average = total / numberOfLines

        print('The average is', average)

main()