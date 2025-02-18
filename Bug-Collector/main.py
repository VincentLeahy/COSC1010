#
# Name: Vincent Leahy
# Date: 2/18/2025
# Bug Collector Programming Project
# COSC 1010
#
# Initialize variables for bugs and total number of bugs collected.

# Get number of bugs collected each day using a for loop.

# Display the total number of bugs collected.

# Initialize the accumulotor.

#Varibles

total = 0
bugs = 0

#Get the bugs collected for each day.

#range value is up to not including ie 1-5 must be typed out 1-6
#as it does not include the 6 so it displays as 1-5.

#prompt User
for day in range (1, 6):
    print("Enter the bugs collected on day", day)

    #input number of bugs.
    bugs = int(input())

    #add bugs collected that day to total.,
    total += bugs

#Display the total bugs collected over 5 days.

print("You collected a total of ", total, "bugs.")