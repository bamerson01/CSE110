# This program stores a list of products in a shopping cart along with their prices. The user will have the ability to add items to the list, remove them, and see the total price of the cart.

add_item = ''
remove_item = ''
quit = ''
choice = None

options_menu = ['Add Item', 'View Cart (empty)', 'Remove Item', 'Cart Total', 'Quit']
items_menu = ['hat', 'shirt', 'sweater', 'pants', 'shorts', 'socks', 'shoes']
items_cart = []
items_price = []

# Displays welcome message and options menu. 
print('\nWelcome to the shopping cart program!')
while choice != '5':
    if len(items_cart) >= 1:
        options_menu[1] = f'View Cart ({len(items_cart)} items)'
    elif len(items_cart) < 1:
        options_menu[1] = f'View Cart (empty)'
    print(f'\nPlease select one of the following:')
    for i, option in enumerate(options_menu):
        print(f'{i+1}. {option}')
    choice = input(f'Please enter the number: ')

# Allows user to add item and it's price to thier cart. item and privce are stored in seperate lists.
    if choice == '1':
        continue_adding = 'yes'
        while continue_adding.lower() != 'no':
            # Displays product listing.
            print(f'\nHere are the items for sale:')
            for i, item in enumerate(items_menu):
                print(f'{item.capitalize()}')
            # Request user input on product to add
            add_item = input(f'\nWhat item would you like to add? ')
            # Validate that input is an offering from our list
            for item in items_menu:
                if  item.lower() == add_item.lower():             
                    items_cart.append(add_item)
                    item_price = float(input(f'What is the price of the {add_item}? $'))
                    items_price.append(item_price)
                    print(f'\n{add_item.capitalize()} has been added to the cart.')
                    continue_adding = input(f'Continue adding items?(yes/no) ')
                #else:
                #    print(f'\nSorry, we don\'t offer that. Please select an item from our product list.')
                 #   break
# Allows user to view thier cart.
    elif choice == '2':
        # Validates if cart is empty and alerts user
        if len(items_cart) < 1:
            print(f'\nYour cart is empty.')
        else:
            print(f'\nThe contents of your cart are:')
            for i, item in enumerate(items_cart):
                item = items_cart[i]
                item_price = items_price[i]
                print(f'{i+1}. {item.capitalize()} - ${item_price:.2f}')

# Allows user to remove item from cart.
    elif choice == '3':
        # Validate if there are items in cart if empty alert cart is empty and return to main options
        if len(items_cart) < 1:
            print(f'\nYour cart is empty. There are no items to remove.')
        else:
            # Display items in cart to select
            print(f'\nWhich item would you like to remove?')
            for i, item in enumerate(items_cart):
                item = items_cart[i]
                item_price = items_price[i]
                print(f'{i+1}. {item.capitalize()} - {item_price:.2f}')
            in_range = False
            while in_range == False:
                # Prompt user to select which index number to remove
                remove_item = int(input(f'\nType the number to remove: '))
                # Validate that user did not input anything outside the index range of the list
                if remove_item - 1 >= 0 and remove_item - 1 <= len(items_cart) - 1:
                    in_range = True
                    items_cart.pop(remove_item-1)
                    items_price.pop(remove_item-1)
                    print('Item removed.')
                else:
                    print('Sorry that is an valid item number. Please try again.')

# Allows user to compute total.
    elif choice == '4':
        sum_total = 0
        for price in items_price:
            sum_total += price
        print(f'\nYour shopping cart total is ${sum_total:.2f}')

# Allows user to quit the application
    elif choice == '5':
        print(f'\nThank you, goodbye!')
# Displays if invalid input
    else:
        print(f'\nNot a valid option, please enter a number of an option')
