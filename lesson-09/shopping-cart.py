# This program stores a list of products in a shopping cart along with their prices. The user will have the ability to add items to the list, remove them, and see the total price of the cart.


options_menu = ['Add Item', 'View Cart',
                'Remove Item', 'Compute Total', 'Quit']
items_menu = ['hat', 'shirt', 'sweater', 'pants', 'shorts', 'socks', 'shoes']
items_cart = []
items_price = []

add_item = ''
view_cart = ''
remove_item = ''
sum_total = ''
quit = ''
choice = None
continue_adding = 'yes'

print()
print('Welcome to the shopping cart program!')
print()
while choice != '5':
    print('Please select one of the following:')
    for i, option in enumerate(options_menu):
        print(f'{i+1}. {option}')
    choice = input('Please enter the number: ')
    print()

    if choice == '1':  # Allows user to add items to cart.
        while continue_adding.lower() != 'no':
            print('Here are the items for sale:')
            for i, item in enumerate(items_menu):  # Displays product listing.
                print(f'{item.capitalize()}')
            print()
            add_item = input('What item would you like to add? ')
            items_cart.append(add_item)
            continue_adding = input(
                'Would you like to continue adding items to the cart?(yes/no) ')
    elif choice == '2':  # Allows user to view thier cart.
        print('The contents of your cart are:')
        for item in items_cart:
            print(item)
    # elif choice == 3 # Allows user to remove item from cart.
    # elif choice == 4 # Allows user to compute total.
    elif choice == '5':
        print('Thank you, goodbye!')
    else:
        print('Not a valid option, please enter the number of an option')
