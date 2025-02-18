#
# Name: Vincent Leahy
# Date: 2/18/2025
# Budget Analysis Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

#Declare Variables, Budget Amount, Amount Spent, Difference, and Total
Budget = 0.0
Difference = 0.0
#Spent must = a number as you cannot spend 0.0 dollars
Spent = 1.0 #initalize for the while loop
Total = 0.0

#Get the budgeted amount from the user
Budget = float(input("Enter amount budgeted for the month:" ))

#Get the total amount spent from the user, this is also where the loop is,
#but after putting the number you spent you will be promted again simply put 0,
#that will release you from the loop, or that is the solution I figured out. 
while True: 
    Spent = float(input("Enter an amount spent(0 to quit): "))
    if Spent == 0:
        break 
#add the total
    Total += Spent

#Determine wether the user is over or under budget and display the results.
print ("Budgeted: $", format(Budget, '.2f'))
print ("Spent: $", format(Total, '.2f'))

#Create the if, elif, else statments.
if Budget > Total:
    Difference = Budget - Total
    print ("You are $", format(Difference, '.2f'), "under budget. Well Done!")
elif Budget < Total:
    Difference = Total - Budget
    print ("You are $", format(Difference, '.2f'), "over budget. Plan Better next time!")
else:
    print ("Spending matchest budget. Good Planning!")
