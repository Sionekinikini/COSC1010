#
# Sione Kinikini
# 2/23/25
# Kilometer Converter Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

# Conversion Factor
conversion_factor = 0.6214

# Main function gets the kilometers and calls the show_miles function to convert to miles
def main():
    # Get distance in kilometers
    kilometers = float(input('Enter distance in Kilometers:'))

    # Display miles to kilometers
    show_miles(kilometers)

# Show_miles function converts the distance from kilometers to miles
def show_miles(km):
    # Calculate miles
    show_miles = km * conversion_factor

    # Display miles
    print(km, 'kilometers equals', show_miles, 'miles')

# Call the main function
main()