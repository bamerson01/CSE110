accounts = []
balances = []
account = ''
balance = ''

# Allows user to add accounts and balance ammount until user types quit. Stores account name and balance in seperate lists
print('Enter the names and balances of bank accounts (type: quit when done)')
while account.lower() != 'quit':
    account = input('What is the name of this account? ')
    if account.lower() != 'quit':
        accounts.append(account)
        balance = float(input('What is the balance? '))
        balances.append(balance)

# Displays account names and balance ammount for each account that was entered by user
print('\nAccount Information:')
for i, account in enumerate(accounts):
    account = accounts[i]
    balance = balances[i]
    print(f'{i}. {account.capitalize()}: ${balance:.2f}')

# Computes the balance of all accounts and display total.
sum_total = 0
for balance in balances:
    sum_total += balance
print(f'The total balance is: ${sum_total:.2f}')

# Computes the average balance for all accounts and displays info
average = sum_total / len(balances)
print(f'The average balance is: {average:.2f}')

# Evaluates which account has the largest balance and then displays account name and balance
highest_balance = -999
highest_account = None
for i, balance in enumerate(balances):
    balance = balances[i]
    account = accounts[i]
    if balance > highest_balance:
        highest_balance = balance
        highest_account = account
print(f'Highest balance: {account}: {highest_balance}')

# Allows user to make updates to account balances
update_balance = 'yes'
while update_balance.lower() != 'no':
    update_balance = input(
        '\nDo you want to update an account balance?(yes/no) ')
    if update_balance == 'yes':
        what_account = int(input('What account index do you want to update? '))
        new_balance = float(input('What is the new amount? '))
        balances[what_account] = new_balance
        # Displays account names and balance ammount for each account that was entered by user
        print('\nAccount Information:')
        for i, account in enumerate(accounts):
            account = accounts[i]
            balance = balances[i]
            print(f'{i}. {account.capitalize()}: ${balance:.2f}')
    else:
        print('Have a great day!')
