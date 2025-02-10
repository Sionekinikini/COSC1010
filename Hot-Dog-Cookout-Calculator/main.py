#
# Sione Kinikini
# 2/9/25
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

# Variables
import math
guests = int(input('Number of guests attending: '))
hot_dogs_per_person = int(input('Number of hot dogs per person: '))
hot_dogs_per_package = 10
buns_per_package = 8

# Find the total amount of hot dogs needed and number of packages
total_hot_dogs = guests * hot_dogs_per_person
minimum_total_packages = math.ceil(total_hot_dogs / hot_dogs_per_package)

# Find the total amount of packages of buns needed
minimum_buns_packages = math.ceil(total_hot_dogs / buns_per_package)

# Results
print("Minimum packages of hot dogs:", minimum_total_packages)
print("Minimum packages of buns:", minimum_buns_packages)

# Leftovers
hot_dogs_leftover = minimum_total_packages * 10 - total_hot_dogs
leftover_buns = minimum_buns_packages * 8 - total_hot_dogs

# Results
print("Hot dogs leftover:", hot_dogs_leftover)
print("Buns leftover:", leftover_buns)