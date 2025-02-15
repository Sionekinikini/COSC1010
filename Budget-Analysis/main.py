#
# Sione Kinikini
# 2/15/25
# Budget Analysis Programming Project
# COSC 1010
#

# Get the budget of a user
budget = int(input('Enter the budget of the month: '))

# Variable to control the loop
another = 'y'

# Declare the total
total = 0

# Process the expense
while another == 'y' or another == 'Y':
# Get the expense
    expenses = float(input('Enter the expense: '))
    total += expenses
 # Ask if there is another expense
    another = input('Do you have another expense? ' +
                    '(Enter y for yes): ')

if total > budget:
    print(f'You are ${total - budget} over the budget ')
elif total == budget:
    print(f'Your budget is equal to your expenses')
else:
    print(f'You are ${budget-total} under the budget ')

print(f'Total expenses: ${total}')