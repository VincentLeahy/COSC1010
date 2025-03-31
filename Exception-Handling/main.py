#
# Name Vincent Leahy    
# Date 3/30/2025
# Exception Handling Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

def main():
    # Open the file.
    myfile = open('numbers.txt', 'r')

#creating the Exception handling in regards to the file.
    try:

    # Read and display the files contents.
        for line in myfile:
            myfile = open('numbers.txt', 'r')
    except IOError as errorGenerated:
        print('File not Found:', errorGenerated)
    else:
        total = 0
    numberOfLines = 0
    line = myfile.readline()

    while line != '':
        numberOfLines += 1
        total += int(line)
        line = myfile.readline()

    average = total / numberOfLines

    print('The average is', average)
#Closing the file 
    myfile.close()

main()