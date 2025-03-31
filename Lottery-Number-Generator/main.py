#
# Sione Kinikini
# 3/30/25
# Lottery Number Generator Programming Project
# COSC 1010
#
import random
# Initialize an empty list to store the lottery numbers
lottery_number = []

# Generate seven random numbers in the range 0 to 9
for _ in range(7):
    # Generate a random number between 0 and 9
    number = random.randint(0, 9)
     # Append the number to the list
    lottery_number.append(number)   

# Display the contents of the list
print("Generated lottery number:")
for number in lottery_number:
     # Print each number in the list
    print(number, end=' ')