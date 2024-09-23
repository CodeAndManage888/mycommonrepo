from faker import Faker
import random

def generate_names_and_numbers(gender, year):
    fake = Faker()
    names = set()
    while len(names) < 100:
        if gender == 'female':
            names.add(fake.first_name_female())
        else:
            names.add(fake.first_name_male())

    with open(f'{year}{gender[0]}', 'w') as file:
        for name in names:
            number = random.randint(1, 99999)
            file.write(f'{name},{number}\n')

years = ['2018', '2019', '2020', "2021", "2022", "2023"]
genders = ['female', 'male']

for year in years:
    for gender in genders:
        generate_names_and_numbers(gender, year)