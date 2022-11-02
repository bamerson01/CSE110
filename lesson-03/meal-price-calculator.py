# This program Compute the price of a meal as follows by asking for the price of child and adult meals, the number of each, and then the sales tax rate. Values are computed to determine the total price of the meal. Then, the program asks for the payment amount and computes the amount of change to give back to the customer.


# Prompt User for price of meal for adult and children and how many were purchased, prompt for tax rate.
child_meal = float(input('What is the price of a child\'s meal? '))
adult_meal = float(input('What is the price of an adult\'s meal? '))
child_count = int(input('How many children are there? '))
adult_count = int(input('How many adults are there? '))
tax_rate = float(input('What is the sales tax rate? '))
print()

# Compute values
child_meal_total = child_meal * child_count
adult_meal_total = adult_meal * adult_count
subtotal = child_meal_total + adult_meal_total
sales_tax = tax_rate / 100 * subtotal
total = subtotal + sales_tax
print()

# Compute tip suggestions
twenty_tip = subtotal * .2
eighteen_tip = subtotal * .18
fifteen_tip = subtotal * .15


# Dsiplay Subtotal, tax amount and total amount
total_msg = f'Subtotal: ${subtotal}\nSales Tax: ${sales_tax}\nTotal: ${total}'
print(total_msg)
print()

# prompt user with tip pecentage suggestions and ask how much of a tip they will pay.
tip_sugg = f'Tip suggestions: 20%: ${twenty_tip} 18%: ${eighteen_tip}  15%: ${fifteen_tip}'
print(tip_sugg)
tip = float(input('Tip ammount? '))
print()

# compute new total with tip ammount
new_total = subtotal + sales_tax + tip
new_total_msg = f'Subtotal: ${subtotal}\nTip: ${tip}\nSales Tax: ${sales_tax}\nTotal: ${new_total}'
print(new_total_msg)
print()

# prompt user for ammount they paid and calculate change due.
amount_paid = float(input('Total amount paid? '))
change = amount_paid - new_total
change_msg = f'Change due: ${change}'
print(change_msg)
