# This program determines whether to loan money based on certain criteria.
# First we will set the staus of the loan approva to false.

loan_approved = False

# Next, we will ask for a rating from 1–10 on the following:

print('Please answer the following questions with a rating of 1-10')
loan_amount = int(input('How large is the loan? '))
credit_score = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down payment? '))

# We will now test the input on the following criteria to dtermine approval
# First, check if the loan size is at least 5. If it is, use the following rules:
# If the credit history and income are both at least 7, then the decision is "yes"
# If either the credit history or income is at least 7, then check if the down payment is at least 5, if it is, the decision is "yes", if not, the decision is "no"
# Otherwise (if neither the credit history nor income is at least 7), the decision is "no"
# Otherwise (if the loan is not 5 or greater), use these rules:
# If the credit is less than 4, then the decision is "no"
# Otherwise, check the following:
# If either the income or the down payment is at least 7, the decision is "yes"
# If both the income and the down payment are at least 4, then the answer is "yes"
# Otherwise, the decision is "no"

if loan_amount >= 5:
    if credit_score >= 7 and income >= 7:
        loan_approved = True
    elif (credit_score >= 7 or income >= 7) and down_payment >= 5:
        loan_approved = True
    else:
        loan_approved = False
else:
    if credit_score < 4:
        loan_approved = False
    elif income >= 7 or down_payment >= 7:
        loan_approved = True
    elif income >= 4 and down_payment >= 4:
        loan_approved = True
    else:
        loan_approved = False

# We will now display if the loan has been approved or not.
if loan_approved:
    print('Your loan is approved!')
else:
    print('Sorry, your loan is not approved.')
