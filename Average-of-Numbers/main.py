#
# Sione Kinikini
# Date 3/26/25
# Average of Numbers Programming Project
# COSC 1010
#
# Main function
def calculate_average(filename):
    with open(filename) as file:
        numbers = [int(line) for line in file]
    print(f"The average is: {sum(numbers) / len(numbers)}")

filename = input("Enter the filename: ")
calculate_average(filename)