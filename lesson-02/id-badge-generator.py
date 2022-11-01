# ID Badge Generator
# Prompt user for information and store it in variables
print('Please enter the following information:')
first_name = input('First name: ')
last_name = input('Last name: ')
email_address = input('Email address: ')
phone_num = input('Phone number: ')
job_title = input('Job title: ')
id_num = input('ID number: ')

# Use stored variables to Generate ID card with the following format
# The ID Card is:
# ----------------------------------------
# DOE, Jane
# Chief Software Architect
# ID: 83-23821
#
# janedoe@email.com
# (208) 555-1234
# ----------------------------------------

output = f'The ID Card is : \n----------------------------------------\n{last_name.upper()}, {first_name.capitalize()}\n{job_title.title()}\nID: {id_num}\n\n{email_address.lower()}\n{phone_num}\n----------------------------------------'

# Print ID Card
print(output)
