min_life = 999.99
min_year = None
min_country = ''

max_life = -1.99
max_year = None
max_country = ''

chosen_avg_expect = 0
chosen_max_expect = 0
chosen_max_country = ''
chosen_min_expect = 999.99
chosen_min_country = ''
sum_life = 0
line_count = 0

# search_by = ['year','country', 'quit']
print('Please type which years you would like to evaluate.')
start_year = int(input('Enter the start year of interest: '))
end_year = int(input('Enter the end year of interest: '))

# Opens CSV data file and parses data into usable list format
with open('life-expectancy.csv') as file:
    for i, line in enumerate(file):
        line = line.strip()
        data_list = line.split(',')
        countries = data_list[0]
        country_codes = data_list[1]
        years = int(data_list[2])
        life_expect = float(data_list[3])

        # Calculates the overall maximum life expectancy across all years 
        if max_life < life_expect:
            max_life = life_expect
            max_country = countries
            max_year = years
        
        # Calculates the overall minimum life expectancy across all years
        if min_life > life_expect:
            min_life = life_expect
            min_country = countries
            min_year = years
        
        # Calculates the average life expectancy across all countries for the chosen year        
        if start_year <= years and end_year >= years:
            line_count += 1 
            sum_life += life_expect
            chosen_avg_expect =  sum_life / line_count

        # Calculates which country had the maximum life expectancy for the chosen year
        if start_year <= years and end_year >= years and chosen_max_expect < life_expect:
            chosen_max_expect = life_expect
            chosen_max_country = countries
            chosen_max_year = years
        
        # Calculates which country had the minimum life expectancy for the chosen year
        if start_year <= years and end_year >= years and chosen_min_expect > life_expect:
            chosen_min_expect = life_expect
            chosen_min_country = countries
            chosen_min_year = years

# while search_by != 
# print('Please select a search option:')
# search_by = input(f'\n Search by:')
       

print(f'\nThe overall maximum life expectancy was: {max_life:.2f} years from {max_country} in {max_year}.')
print(f'The overall minimum expectancy was: {min_life:.2f} years from {min_country} in {min_year}.')
print(f'\nFor the years {start_year} - {end_year}:')
print(f'The average life expectancy across all countries was {chosen_avg_expect:.2f} years.')
print(f'The max life expectancy was: the year {chosen_max_year} in {chosen_max_country} at {chosen_max_expect:.2f} years.')
print(f'The min life expectancy was: {chosen_min_year} in {chosen_min_country} at {chosen_min_expect:.2f} years')
print()