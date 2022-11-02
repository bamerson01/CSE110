# This program asks the user for a series of words and then displays the story with the user's words inserted into the appropriate places.

# Ask user for various words. Words are then stored in variables to use in story
print('Please enter the following:')
adjective = input('adjective: ')
animal = input('animal: ')
verb1 = input('verb: ')
exclamation = input('exclamation: ')
verb2 = input('verb: ')
verb3 = input('verb: ')
color = input('color: ')
nickname = input('nickname: ')
city = input('city: ')
noun = input('thing: ')

# check if the input for noun starts with a vowel to determine if word should have 'a' or 'an' before the word
if noun[0].lower() in ['a', 'e', 'i', 'o', 'u']:
    is_vowel = 'an'
else:
    is_vowel = 'a'


# this function determines if verb should have the word 'to' before it. Checks if verb is greater than 5 characters to prevent false positives with words such as sing, bring, etc. If verb does not end with the suffix "ing" and greater than 5 character we will add the word 'to' before the verb

def add_to(verb):
    if len(verb) > 4 and (verb).endswith('ing'):
        return (verb)
    else:
        return "to " + (verb)


# generate story with stored variables
mad_lib = f'The other day, I was really in trouble. It all started when I saw a very {adjective.lower()} {animal.lower()} {verb1.lower()} down the hallway. "{exclamation.capitalize()}!" I yelled. But all I could think to do was {add_to(verb2.lower())} over and over. Miraculously, that caused it to stop, but not before it tried {add_to(verb3.lower())} right in front of my family. I then tried to catch it but as soon as I touched it my hand turned {color.lower()}. How strange, I thought, and then things got more weird. The {animal.lower()} started talking to me. It said it\'s name was {nickname.capitalize()} and it had magical powers. {nickname.capitalize()} said that to remove the {color.lower()} off my hand I would need to journey to the magical land of {city.title()} to find {is_vowel} {noun.lower()}. Once I obtained the {noun.lower()} my hand would return back to normal.'

# print story
print(mad_lib)
