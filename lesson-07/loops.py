# This program uses a while loop to ask the user for a positive number (>= 0). Continue asking as long as the number is negative, then display the number.

number = int(input('Please type a postive number: '))

while number < 0:
    print('Sorry, that is a negative number. Please try again.')
    number = int(input('Please type a postive number: '))

print(number)

# This program uses a while loop, to simulate a child asking their parent for a piece of candy. Have the program keep looping until the user answers "yes", then have the program output "Thank you."

have_candy = input('Can I have peice of candy? ')

while have_candy.lower() != 'yes':
    have_candy = input('Please, can I have peice of candy? ')

print('Thanks!')
