# This program stores a secret word that the user must guess. The user must enter the same amount of letters as the word. After each guess the program will display any letters in the word that they guessed that are in the secret word. If the guess has a letter in the same postion as the secret word the letter will display in hint with a capital format. If the word guessed has letters that are in the secret word but not in the same location as the seceret word the letters will display in lower case. Any letters not guessed will display as a underscore.

# Import the URL Library to fetch content from a URL for our secret word generator
from urllib.request import Request, urlopen
import random

secret_word = ''
guess = ''
guess_count = 0

# SECRET WORD GENERATOR
# This will scrape content from a webpage and seperate the words into a list. We then select a random sample from the list to choose a secret word.
url = "http://www.mit.edu/~ecprice/wordlist.10000"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_content = webpage.decode('utf-8')
word_split = page_content.split("\n")
word_list = random.sample(word_split, 10)
for word in word_list:
    if len(word) == 5 and word.isalpha():
        secret_word = word.lower()

hint = '_' * len(secret_word)

# print(secret_word)

# Prompt the user for a guess and continue looping as long as that guess is not correct. Calculates number of guesses and displays count upon answering correctly.
print()
print('Welcome to the word guessing game.')
print()
while guess != secret_word:
    guess_count = guess_count + 1
    print(f'Your hint is: {hint}')
    print()
    guess = input(f'Guess the secret word: ')
    if len(guess) != len(secret_word):
        print('Sorry, the guess must have the same number of letters as the secret word.')

    for i, letter in enumerate(guess):
        for j, char in enumerate(secret_word):
            #print(i, j, letter, char)
            if i == j and letter == char:
                print(letter.upper(), end='')
            elif i != j and letter == char:
                print(letter.lower(), end='')
        else:
            print('_', end='')
    print()
else:
    print('Congratulations! You guessed it!')
    print(f'It took you {guess_count} guesses')
