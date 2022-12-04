import random

play = 'yes'
magic_number = -1
best_score = 20

while play.lower() == 'yes':
    magic_number = random.randint(1, 20)
    guess = int(input('Guess the magic number. Pick a number between 1-20: '))
    guess_count = 1

    while guess != magic_number:
        guess_count = guess_count + 1
        if guess > magic_number:
            guess = int(input('Lower, guess again: '))
        if guess < magic_number:
            guess = int(input('Higher, guess again: '))

    if guess_count < 2:
        success_msg = 'You got it on the first try!'
    else:
        success_msg = f'You got it! It took you {guess_count} attempts.'

    if guess_count <= best_score:
        best_score = guess_count
        best_msg = f'You just achieved a new best score!'
    else:
        best_msg = f'Your best score is {best_score}'

    print(success_msg)
    print(best_msg)
    play = input('Do you want to play again? (yes/no) ')
print('Thanks for playing')
