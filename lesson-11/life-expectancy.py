with open('life-expectancy.csv') as le_file:
    for line in le_file:
        line = line.strip()
        data_piece = line.split(',')
        print(data_piece)
        country = data_piece[0]
        country_code = data_piece[1]
        year = data_piece[2]
        life_expect = data_piece[3]
        lowest_life = 999
        # for data in life_expect:
        #     if lowest_life > data:
        #         lowest_life = data
        print(life_expect + 1)
    