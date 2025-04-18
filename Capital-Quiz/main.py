#
# Name
# Date
# Capital Quiz Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random

def main():
    # Initialize dictionary of states and their capitals
    capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau',
                'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
                'California': 'Sacramento', 'Colorado': 'Denver',
                'Connecticut': 'Hartford', 'Delaware': 'Dover',
                'Florida': 'Tallahassee', 'Georgia': 'Atlanta',
                'Hawaii': 'Honolulu', 'Idaho': 'Boise',
                'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
                'Iowa': 'Des Moines', 'Kansas': 'Topeka',
                'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
                'Maine': 'Augusta', 'Maryland': 'Annapolis',
                'Massachusetts': 'Boston', 'Michigan': 'Lansing',
                'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
                'Missouri': 'Jefferson City', 'Montana': 'Helena',
                'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
                'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
                'New Mexico': 'Santa Fe', 'New York': 'Albany',
                'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
                'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
                'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
                'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
                'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
                'Texas': 'Austin', 'Utah': 'Salt Lake City',
                'Vermont': 'Montpelier', 'Virginia': 'Richmond',
                'Washington': 'Olympia', 'West Virginia': 'Charleston',
                'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

    # Local variables to track score
    correct = 0
    incorrect = 0

    # List of states to randomly pick from
    states = list(capitals.keys())

    print("Welcome to the U.S. State Capitals Quiz!")
    print("Type 'exit' anytime to quit.\n")

    # Continue until the user quits the game
    while True:
        # Pick a random state
        state = random.choice(states)
        # Ask the user for the capital of the chosen state
        user_answer = input(f"What is the capital of {state}? ").strip()

        # Allow user to exit
        if user_answer.lower() == 'exit':
            break

        # Check if the answer is correct (case-insensitive)
        if user_answer.lower() == capitals[state].lower():
            print("Correct!\n")
            correct += 1
        else:
            print(f"Incorrect. The capital of {state} is {capitals[state]}.\n")
            incorrect += 1

    # Show the final results
    print("\nQuiz Finished!")
    print(f"Total correct answers: {correct}")
    print(f"Total incorrect answers: {incorrect}")

# Call the main function
main()
