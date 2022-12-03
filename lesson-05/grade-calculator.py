grade_percentage = int(input('What is your grade percentage? '))

if grade_percentage >= 90 and grade_percentage <= 100:
    letter = 'A'
elif grade_percentage >= 80 and grade_percentage <= 89:
    letter = 'B'
elif grade_percentage >= 70 and grade_percentage <= 79:
    letter = 'C'
elif grade_percentage >= 60 and grade_percentage <= 69:
    letter = 'D'
else:
    letter = 'F'

if grade_percentage >= 70:
    pass_fail = 'Congratulations, you passed the class!'
else:
    pass_fail = 'Infortunately that is not a high enough score to pass the class. Please try again.'


if grade_percentage % 10 >= 7:
    plus_minus = '+'
elif grade_percentage % 10 <= 3:
    plus_minus = '-'
else:
    plus_minus = ''

if grade_percentage >= 93:
    plus_minus = ''

if letter == 'F':
    plus_minus = ''

msg = f'Your letter grade is an {letter}{plus_minus}.\n{pass_fail}'

print(msg)
