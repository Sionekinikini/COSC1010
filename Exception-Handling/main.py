#
# Sione Kinikini
# 3/26/25
# Exception Handling Programming Project
# COSC 1010
#
# Main function
def calculate_average(filename):
    try:
        with open(filename, 'r') as file:
            numbers = []
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(f"Warning: '{line.strip()}' is not a valid number and will be ignored.")
        
        if not numbers:
            print("Error: No valid numbers found in the file.")
            return

        average = sum(numbers) / len(numbers)
        print(f"The average of the numbers is: {average}")

# Add exceptions for incorrect input or error
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: An error occurred while reading the file '{filename}'.")

# Get the file name from user input
filename = input("Enter the filename: ")
calculate_average(filename)