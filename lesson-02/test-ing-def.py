verb1 = 'singing'
verb2 = 'laughing'
verb3 = 'sing'


def add_to(verb):
    if len(verb) > 4 and (verb).endswith('ing'):
        return (verb)
    else:
        return "to " + (verb)


print(add_to(verb1))
print(add_to(verb2))
print(add_to(verb3))
