# This program converts Fahrenheit to Celsius and displays the result to one decimal place of precision.
# Example:
# What is the temperature in Fahrenheit? 81
# The temperature in Celsius is 27.2 degrees.

temperature_f = int(input('What is the temperature in Fahrenheit?: '))
temperature_c = (temperature_f - 32) * (5/9)
temperature_answer = f'The temperature in Celsius is {temperature_c:.1f} degrees.'
print(temperature_answer)
