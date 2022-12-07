people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 99
youngest_name = ''

for i, line in enumerate(people):
    person = line.split(' ')
    name = person[0]
    age = int(person[1])

    if youngest_age > age:
        youngest_age = age
        youngest_name = name
print(f'The youngest person is {youngest_name} at {youngest_age} years old')
