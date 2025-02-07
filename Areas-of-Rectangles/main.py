#
# Sione Kinikini
# 2/6/25
# Areas of Rectangles Programming Project
# COSC 1010
#
# Local variables

# Get length A B and Width A B

LengthA = int(input('Length of Rectangle A:'))
WidthA = int(input('Width of Rectangle A:'))
LengthB = int(input('Length of Rectangle B:'))
WidthB = int(input('Width of Rectangle B:'))
# Calculate area A

AreaA = LengthA * WidthA
# Calculate area B

AreaB = LengthB * WidthB
# Print area comparison using if-elif-else statements
if AreaA > AreaB:
    print('Rectangle A has a Greater Area')

elif AreaB > AreaA:
    print('Rectangle B has a Greater Area')

else:
    print('Rectangles Have the Same Area')