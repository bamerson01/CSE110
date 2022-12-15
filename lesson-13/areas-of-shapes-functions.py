import math



# Area of a square - prompts user for length of a side, then multiplies it by itself, then outputs the solution
def compute_square_area (length, width=False):
    if width == True:
        area = length * width
    else:
        area = length ** 2
    return area

square_length = float(input('What is the length of a side of the square? '))
rectangle_length = float(input('What is the length of rectangle? '))
rectangle_width = float(input('What is the width of the rectangle?'))

print(compute_square_area(square_length))
print(compute_square_area(rectangle_length, rectangle_width))