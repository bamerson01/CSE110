guess = 'play'
secret_word = 'pizza'
hint = '_' * len(secret_word)

print(hint)
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
