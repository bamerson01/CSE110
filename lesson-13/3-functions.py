def print_regular(message):
    print(message)

def print_lower(message):
    print(message.lower())

def print_upper(message):
    print(message.upper())

input_message = input(f'What is your message? ')

print_regular(input_message)
print_lower(input_message)
print_upper(input_message)