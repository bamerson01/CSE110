with open('hr_system.txt') as hr_system_file:
    for line in hr_system_file:
        line = line.strip()
        parts = line.split()
        name = parts[0]
        id_number = parts[1]
        job_title = parts[2]
        salary = int(parts[3])
        paycheck = salary / 24
        # print(f'Name: {name}, Title: {job_title}')
        if job_title.lower() == 'engineer':
            paycheck += 1000
        print(f'{name} ({id_number}), {job_title} - ${paycheck:.2f}')
    