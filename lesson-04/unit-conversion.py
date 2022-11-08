# This program converts Fahrenheit to Celsius and displays the result to one decimal place of precision.
# Example:
# What is the temperature in Fahrenheit? 81
# The temperature in Celsius is 27.2 degrees.

temp_f = int(input('What is the temperature in Fahrenheit?: '))
temp_c = (temp_f - 32) * (5/9)
temp_answer = f'The temperature in Celsius is {temp_c:.1f} degrees.'
print(temp_answer)
