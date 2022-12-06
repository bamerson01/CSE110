
shopping_item = ''
shopping_list = []

print('Please enter the items of the shopping list (type: quit to finish):')
while shopping_item.lower() != 'quit':
    shopping_item = input('Item: ')
    if shopping_item.lower() != 'quit':
        shopping_list.append(shopping_item)
print()

print('The shopping list is:')
for item in shopping_list:
    print(item.capitalize())
print()

print('The shopping list with indexes is:')
for i, item in enumerate(shopping_list):
    print(f'{i}. {item.capitalize()}')

change_item = int(input('Which item woud you like to change? '))
new_item = input('What is the new item? ')
shopping_list[change_item] = new_item

print()
print('The shopping list with indexes is:')
for i, item in enumerate(shopping_list):
    print(f'{i}. {item.capitalize()}')
