#
# Sione Kinkini
# 2/23/25
# Feet to Inches Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

# Conversion
inches_per_foot = 12

# Main function
def main():
    # Get the number of feet
    feet = int(input('Enter a number of feet:'))

    # Convert to inches
    print(feet, 'feet equals', feet_to_inches(feet), 'inches.')

# Calulate feet to inches
def feet_to_inches(feet):
    return feet * inches_per_foot

# Call the main function
main()

