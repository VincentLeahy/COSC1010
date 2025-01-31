#
# Name Vincent Leahy
# Date 1/30/2025
# Sales Tax Programming Project
# COSC 1010
#

# Variable declarations
purchase_amount = 0.0
state_tax = 0.0
county_tax = 0.0
total_sales_tax = 0.0
total_sales = 0.0
#I had to define these otherwise the code would not work so I just put 0.0 as a place holder

# Constants for the state and county tax rates
state_tax_rate = 0.05
county_tax_rate = 0.024

# Get the amount of the purchase.
purchase_amount = float(input("Enter the amount of the purchase: "))

# Calculate the state sales tax.
state_tax = purchase_amount * state_tax_rate

# Calculate the county sales tax.
county_tax = purchase_amount * county_tax_rate

# Calculate the total tax.
total_sales_tax = state_tax + county_tax

# Calculate the total of the sale.
total_sale = purchase_amount + total_sales_tax

# Print information about the sale.
print("\nPurchase Amount: $",
format(purchase_amount, ",.2f"))
print("State Sales Tax: $",
format(state_tax, ",.2f"))
print("County Sales Tax: $",
format(county_tax, ",.2f"))
print("Total Sales Tax: $",
format(total_sales_tax, ",.2f"))
print("Total Sale Amount: $",
format(total_sale, ",.2f"))

##using the same style as the Sales prediction programming problem I was albe to just replicate that code. By making more varibles and similar calculations