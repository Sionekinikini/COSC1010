#
# Sione Kinikini
# 1/30/25
# Sales Tax Programming Project
# COSC 1010
#

# Variable declarations

# Constants for the state and county tax rates

# Get the amount of the purchase.
total_amount = float(input('Enter amount of purchase:'))
# Calculate the state sales tax.
state_sales_tax = total_amount * 0.05
# Calculate the county sales tax.
county_sales_tax = total_amount * 0.025
# Calculate the total tax.
total_tax = state_sales_tax + county_sales_tax
# Calculate the total of the sale.
total_sale = total_amount + total_tax
# Print information about the sale.
print('State Sales Tax = $', state_sales_tax)
print('County Sales Tax = $', county_sales_tax)
print('Total Sales Tax = $', total_tax)
print('Total Sale = $', total_sale)