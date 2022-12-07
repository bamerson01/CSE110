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

chosen_year = int(input('Enter the year of interest: '))

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
        if chosen_year == years:
            sum_life += life_expect
            number_countries = data_list[3]
            chosen_avg_expect = sum_life / number_countries

        # Calculates which country had the maximum life expectancy for the chosen year
        if chosen_year == years and chosen_max_expect < life_expect:
            chosen_max_expect = life_expect
            chosen_max_country = countries
        
        # Calculates which country had the minimum life expectancy for the chosen year
        if chosen_year == years and chosen_min_expect > life_expect:
            chosen_min_expect = life_expect
            chosen_min_country = countries


print(f'\nThe overall maximum life expectancy is: {max_life:.2f} from {max_country} in {max_year}.')
print(f'The overall minimum expectancy is: {min_life:.2f} from {min_country} in {min_year}.')
print(f'\nFor the year {chosen_year}:')
print(f'The average life expectancy across all countries was {chosen_avg_expect}')
print(f'The max life expectancy was in {chosen_max_country} with {chosen_max_expect:.2f}')
print(f'The min life expectancy was in {chosen_min_country} with {chosen_min_expect:.2f}')
print()
print(sum_life)
print(number_countries)