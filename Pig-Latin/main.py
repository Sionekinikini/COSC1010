#
# Sione Kinikini
# 4/13/25
# Pig Latin Programming Project
# COSC 1010
#
# Create the pig latin function with the split feature
def piglatin():
    words = input("Input sentence: ").split()
    for word in words:
        print(word[1:] + word[:1] + "ay", end = ' ')

# Call the function
piglatin()
    