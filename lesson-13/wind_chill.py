# This program asks the user for a temperature and then shows the wind chill values for various wind speeds at that temperature.

v = float(5)

# This function converts Celsius to Fahrenheit. 
def celsius_conv (celsius):
    return celsius * (9/5) + 32

# This function calculates and returns the wind chill based on a given temperature and wind speed.
def get_wind_chill (t=32,v=5):
    return 35.74 + t*0.6215 - 35.75 * v**0.16 + (t*0.4275)*(v**0.16)

# Ask user for temperature and measurment scale (F/C)
t = float(input('What is the temperature? '))
measurement_scale = input('Fahrenheit or Celsius (F/C)? ')


if measurement_scale.lower() == 'c':
    t = celsius_conv(t)

# Loops through wind speeds from 5 to 60 miles per hour, incrementing by 5, and calculates and displays the wind chill for each of these wind speeds.
while v <= 60: 
    print(f'At temperature {t}F, and wind speed {v} mph, the windchill is: {get_wind_chill(t,v):.2f}F')
    v += 5

