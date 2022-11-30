# COMPARING NUMBERS
# Write a program that asks the user for two integers.
# Then, write three separate if/else statements as follows:
# If the first number is greater than the second, print "The first number is greater". Otherwise, print "The first number is not greater".
# If the two numbers are equal print "The numbers are equal". Otherwise, print "The numbers are not equal".
# If the second number is greater than the first, print "The second number is greater". Otherwise, print "The second number is not greater".
first_number = int(input('What is the first number? '))
second_number = int(input('What is the second number? '))

if first_number > second_number:
    msg = f'Your first number {first_number} is greater than your second number {second_number}'
elif first_number < second_number:
    msg = f'Your first number {first_number} is less than your second number {second_number}'
else:
    msg = f'Your first number {first_number} equals your second number {second_number}'

print(msg)

# COMPARING STRINGS
# Have the program ask the user for their favorite animal. Then write an if statement as follows:
# Check to see if the user's favorite animal is the same as your favorite animal (meaning you, the programmer). If it is, print "That's my favorite animal too!" If it's not, print "That one is not my favorite." Verify that it works regardless of the capitalization.

user_fav_animal = input('What is your favorite animal? ')
my_fav_animal = 'Owl'

if user_fav_animal.lower() == my_fav_animal.lower():
    print('That is my favorite animal too!')
else:
    print('That is not my favorite animal.')
