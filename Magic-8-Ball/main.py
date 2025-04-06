#
# Sione Kinikini
# 4/6/25
# Magic 8 Ball Programming Project
# COSC 1010
#
import random

# 8-ball responses
responses = [
    "Yes, of course!",
    "Without a doubt, yes.",
    "You can count on it.",
    "For sure!",
    "Ask me later.",
    "I'm not sure.",
    "I can't tell you right now.",
    "I will tell you after my nap.",
    "No way!",
    "I don't think so.",
    "Without a doubt, no.",
    "The answer is clearly NO."
]

print("Welcome to the Magic 8 Ball!")
print("Ask a yes or no question. Type 'quit' to exit.")

# Main loop
question = ""
while question.lower() != "quit":
    question = input("What is your question?")
    if question.lower() != "quit":
        index = random.randint(0, len(responses) - 1)
        print("Magic 8 Ball says:", responses[index])

print("Goodbye!")