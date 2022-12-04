# This progam determines if a guest can ride this ride based on the following criteria:
# No one under 36 inches may ever ride, either by themselves or with another rider.
# Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.
# If there are two riders and one of them is at least 18 years old, they may ride together.

# Additional Criteria
# If there are two riders, but neither one is at least 18 years old, they may still ride as long as they are both at least 12 years old and at least 52 inches tall.
# If a person is age 12–17, ask if that person has a golden passport. If they do, they should be treated as if they were 18 years old for the sake of all rules. (Don't forget to apply this to the single rider case.)
# If there are two riders, but neither one is at least 18 years old, they may still ride if one rider is at least 16 years old and the other is at least 14. (Keep in mind that the first rider may be the younger of the two or they may be the older of the two.)

can_ride = False

first_rider_age = int(input('What is age of the first rider? '))
if first_rider_age >= 12 and first_rider_age <= 17:
    golden_passport = input('Do you have a golden passport?(yes/no) ')
    if golden_passport.lower() == 'yes':
        first_rider_age = 18
first_rider_height = int(input('What is the height of the first rider? '))
is_second_rider = input('Is there a second rider (yes/no)? ')
if is_second_rider.lower() == 'yes':
    second_rider_age = int(input('What is the age of the second rider? '))
    second_rider_height = int(
        input('What is the height of the second rider? '))
    if first_rider_height < 36 or second_rider_height < 36:
        can_ride = False
    elif first_rider_age < 18 and second_rider_age < 18:
        can_ride = False
    else:
        can_ride = True
elif is_second_rider.lower() == 'no':
    if first_rider_age >= 18 and first_rider_height >= 62:
        can_ride = True
    else:
        can_ride = False
else:
    print('Incorrect input, please start over.')

if can_ride:
    print('Welcome to the ride. Please be safe and have fun!')
else:
    print('Sorry, you may not ride.')
