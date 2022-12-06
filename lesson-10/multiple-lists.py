accounts = []
balances = []
account = ''
balance = ''

print('Enter the names and balances of bank accounts (type: quit when done)')
while account.lower() != 'quit':
    account = input('What is the name of this account? ')
    if account.lower() != 'quit':
        accounts.append(account)
        balance = float(input('What is the balance? '))
        balances.append(balance)

print('Account Information:')
for i, account in enumerate(accounts):
    account = accounts[i]
    balance = balances[i]
    print(f'{i}.{account.capitalize()}: ${balance:.2f}')

sum_total = 0
for balance in balances:
    sum_total += balance

print(f'The total balance is: ${sum_total:.2f}')

average = sum_total / len(balances)

print(f'The average balance is: {average:.2f}')

largest_balance = 0
for i, balance in enumerate(balances):
    balance = balances[i]
    account = accounts[i]
    if balance > largest_balance:
        largest_balance = balance
    print(f'Highest balance: {account}: {largest_balance}')


update_balance = input('Do you want to update an account balance?(yes/no) ')
while update_balance.lower() != 'no':
    what_account = input('What account index do you want to update? ')
    new_balance = float(input('What is the new amount? '))
    balances[what_account] = new_balance
