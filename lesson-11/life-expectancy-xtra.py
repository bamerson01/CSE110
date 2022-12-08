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
selected_countries = []
sum_life = 0
line_count = 0

# search_by = ['year','country', 'quit']
print('Please type which years you would like to evaluate.')
start_year = int(input('Enter the start year of interest: '))
end_year = int(input('Enter the end year of interest: '))
while add_country.lower() != 'all' or add_country.lower() != 'end':
    print('Please type the countries you would like to evaluate. Type ALL for all countries and END to finish')
    add_country = input(f'Country: ')
    if add_country.lower() != 'end':
        selected_countries.append(add_country)


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
       

print(f'\nThe overall maximum life expectancy is: {max_life:.2f} from {max_country} in {max_year}.')
print(f'The overall minimum expectancy is: {min_life:.2f} from {min_country} in {min_year}.')
print(f'\nFor the years {start_year} - {end_year}:')
print(f'The average life expectancy across all countries was {chosen_avg_expect:.2f}')
print(f'The max life expectancy is: {chosen_max_year} in {chosen_max_country} with {chosen_max_expect:.2f}')
print(f'The min life expectancy is: {chosen_min_year} in {chosen_min_country} with {chosen_min_expect:.2f}')
print()
print(sum_life)
print(line_count)