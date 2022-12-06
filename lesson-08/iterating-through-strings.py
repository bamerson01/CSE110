# This program asks the user for their favorite letter. Then, loops through a programmed word one letter at a time. If the letter in the programmed word is the user's favorite, the program prints it out as a capital letter, if not, it prints it out as a lower case letter.

word = 'commitment'
fav_letter = input('What is your favorite letter? ')

for letter in word.lower():
    if fav_letter.lower() == letter:
        letter = letter.upper()
    print(letter, end='')
print()

for letter in word.lower():
    if fav_letter.lower() == letter:
        letter = '_'
    print(letter, end='')
print()

quote = 'In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost.'
play_again = 'yes'

while play_again.lower() == 'yes':
    number = int(input('What is your favorite single digit number? '))
    for i, letter in enumerate(quote):
        if i % number == 0:
            print(letter.upper(), end='')
        else:
            print(letter.lower(), end='')
    print()
    play_again = input('Do you want to play again?(yes/no) ')
print('Thanks for playing')
