# Prompt the user for their age. Convert it to a number, add one to it, and tell them how old they will be on their next birthday.
age = input('How old are you? ')
next_age = int(age) + 1

age_message = f'On your next Birthday, you will be {next_age} years old.'

print(age_message)
print()

# Prompt the user for the number of egg cartons they have. Assume each carton holds 12 eggs, multiply their number by 12, and display the total number of eggs.
egg_cartons = input('How many egg cartons do you have? ')
eggs = int(egg_cartons) * 12

egg_message = f'You have {eggs} eggs'

print(egg_message)
print()

# Prompt the user for a number of cookies and a number of people. Then, divide the number of cookies by the number of people to determine how many cookies each person gets.
cookies = input('How many cookies are there? ')
people = input('How many people are there? ')
cookie_per_person = int(cookies) / int(people)

cookie_message = f'Each person may have {cookie_per_person} cookies'

print(cookie_message)
