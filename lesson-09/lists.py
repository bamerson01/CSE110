# Ask the user for the names of their friends and append them to a list. Then, display each of the friends in the list. You should stop asking for friends when the user types "end".

friends = []
name = None

while name != 'end':
    name = input('What is the name of a friend? ')
    if name != 'end':
        friends.append(name)

for friend in friends:
    print(friend)
