#
# Name Vincent Leahy
# Date 2/9/2023
# Areas of Rectangles Programming Project
# COSC 1010
#
#dimensions of Rec1
length1 = int(input("Enter the Length of Rectangel 1: "))
width1 = int(input("Enter the width of rectangle 1: "))

#Get dimientions of Rec2
length2 = int(input("Enter the length of rectangle 2: "))
width2 = int(input("Enter the width of rectangle 2: "))

#calculatge the areas of the recs.
area1 = length1 * width1
area2 = length2 * width2

#Determine which has the greeater area.
if area1 > area2:
    print("Rectangle 1 has the greater area.")
elif area2 > area1:
    print("Rectangle 2 has the greater area.")
else:
    print("Both the same area.")