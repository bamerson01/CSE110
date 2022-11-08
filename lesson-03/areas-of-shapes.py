# This program computes the areas of three different shapes: Square, Rectangle, Circle
#
#
# What is the length of a side of the square? 5
# The area of the square is: 25.0
# What is the length of rectangle? 6
# What is the width of the rectangle? 7
# The area of the rectangle is: 42.0
# What is the radius of the circle? 5
# The area of the circle is: 78.5

# import the math library
import math

# Area of a square - prompts user for length of a side, then multiplies it by itself, then outputs the solution
square_length = float(input('What is the length of a side of the square? '))
square_area = square_length ** 2
square_cubed = square_length ** 3
square_response = f'The area of the square is: {square_area}\nThe cubic volume of the square is: {square_cubed}'
print(square_response)
print()

# Area of a rectangle - prompts user for the length and width of the rectangle, multiplies the length and width, then outputs solution
rectangle_length = float(input('What is the length of rectangle? '))
rectangle_width = float(input('What is the width of the rectangle?'))
rectangle_area = rectangle_length * rectangle_width
rectangle_response = f'The area of the rectangle is: {rectangle_area}'
print(rectangle_response)
print()

# Area of a circle - prompts user for the radius of the circle, multiplies radius by pi 3.14, outputs solution
circle_radius = float(input('What is the radius of the circle? '))
circle_area = (circle_radius ** 2) * math.pi
sphere_volume = (4/3) * math.pi * (circle_radius ** 3)
circle_response = f'The area of the circle is: {circle_area}\nThe volume of a sphere is: {sphere_volume}'
print(circle_response)

# circumference = 2πr
# sphere volume = V = ⁴⁄₃πr³
