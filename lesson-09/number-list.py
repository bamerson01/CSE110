# This program asks the user for a series of numbers and appends each one to a list. Stops when they enter 0. Then computes the sum, the average of the numbers in the list, and finds the maximum number in the list.

numbers = []
number = None

print('Enter a list of numbers, type 0 when finished.')

while number != 0:
    number = int(input('Enter a number: '))
    if number != 0:
        numbers.append(number)

sum = 0
for number in numbers:
    sum += number
print(f'The sum is: {sum}')

count = len(numbers)
average = sum / count

print(f'The average is: {average}')

maximum = 0

for number in numbers:
    if number > maximum:
        maximum = number

print(f'The maximum is: {maximum}')

minimum = 999999999999999

for number in numbers:
    if number > 0 and number < minimum:
        minimum = number

print(f'The minimum number is: {minimum}')

sorted_list = sorted(numbers)

print('The sorted list is:')
for number in sorted_list:
    print(number)
