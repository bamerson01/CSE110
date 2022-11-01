# ID Badge Generator
# Prompt user for information and store it in variables
print('Please enter the following information:')
first_name = input('First name: ').strip()
last_name = input('Last name: ').strip()
email_address = input('Email address: ').strip()
phone_num = input('Phone number: ').strip()
job_title = input('Job title: ').strip()
id_num = input('ID number: ').strip()
hair_color = input('Hair color: ').strip()
eye_color = input('Eye color: ').strip()
month_started = input('Month started: ').strip()
training_completed = input('Training completed? (Yes/No): ')

# Use stored variables to Generate ID card with the following format
# The ID Card is:
# ----------------------------------------
# DOE, Jane
# Chief Software Architect
# ID: 83-23821

# janedoe@email.com
# (208) 555-1234

# Hair: Brown           Eyes: Blue
# Month: September      Training: Yes
# ----------------------------------------

id_badge = 'The ID Card is: \n'+'-'*40 + \
    f'\n{last_name.upper()}, {first_name.capitalize()}\n{job_title.title()}\nID: {id_num}\n\n{email_address.lower()}\n{phone_num}\n\nHair: {hair_color.capitalize():15} Eyes: {eye_color.capitalize()}\nMonth: {month_started.capitalize():15}Training: {training_completed.capitalize()}\n'+'-'*40

# Print ID Badge
print(id_badge)
