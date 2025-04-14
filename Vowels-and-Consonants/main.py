#
# Sione
# 4/13/35
# Vowels and Consonants Programming Project
# COSC 1010
#
# Main Function
def main():
    # Input from user
    user_inp = input("Enter a list of characters:")

    # Respond with the number of vowels and consonants
    print("The list has", num_vowels(user_inp), "vowels and", num_consonants(user_inp), "consonants.")
# Function to count the vowels
def num_vowels(s):
    # Create a list of vowels
    vowels = ('a','e','i','o','u')
    # Initialize the accumulator
    v_count = 0
    # For loop to count the vowels
    for ch in s:
        if ch.lower() in vowels:
            v_count += 1

    # Return vowel count
    return v_count

# Function to count consonants
def num_consonants(s):
    # Repeat list of vowels
    vowels = ('a', 'e','i','o','u')

    # Consonant accumulator
    c_count = 0

    # Count the consonants
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            c_count += 1

    # Consonant count return
    return c_count

# Call main function
main()