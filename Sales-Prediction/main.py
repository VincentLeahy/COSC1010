#
# Name Vincent Leahy
# Date 1/30/2025
# Sales Prediction Programming Project
# COSC 1010
#

##Get the projected total sales
##Input the total sales
##Calculate the profit as 23 percent of total sales
##Display the profit

	total_sales = float(input("Enter the projected Sales: "))


##Input = reads a numerical input from keybaord and turns it into a string
## Float = converts the value to a float i.e rounds up
##total_sales executes what ever value was inputed by the user and floated. 


	##profit calculation based on a 23 percent of sales.
	profit = total_sales * 0.23

	##Display and format the profit
	print("The profit is $", format(profit, ",.2f"))

