# Functions: Create a program that defines a function to calculate the area of a circle based on the radius entered by the user.

import math

# Function to calculate the area of a circle
def calculate_area(radius):
    return math.pi * radius ** 2

# Prompt the user for the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate and display the area
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is: {area:.2f}")