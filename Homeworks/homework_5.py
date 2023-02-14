
# Task 1
visited_cities = set(input('Enter the cities you visited in the past 10 years:').lower().split())
future_cities = set(input('Enter the cities you want to visit in the next 10 years:').lower().split())

common_cities = visited_cities.intersection(future_cities)

if not common_cities:
    print('You are open to new experiences!')
else:
    cities = ', '.join(common_cities).title()
    print('You really enjoyed these cities!', cities)

# Task 2

from pprint import pprint

student = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}

student.update({
        'Гаррі Пoттер': {
        'Пошта': 'potter@gmail.com',
        'Вік': 22,
        'Номер телефону': '+380991112233',
        'Середній бал': 99
        }
})
pprint(student, width = 30)

top_students = []
avg = []
for name, rate in student.items():
    if rate['Середній бал'] > 90:
        top_students.append((name, rate['Середній бал']))
        avg.append(rate['Середній бал'])
print('Список студентів з середнім балом більше 90:')
for name, rate in top_students:
    print(name, rate)

sum = sum(avg)
result = sum/len(avg)
print('Середній бал у групі', result)

for name, phone in student.items():
    if phone['Номер телефону'] is None:
        phone['Номер телефону'] = '+38111111111'
        print(f"У студента {name} відстутній номер телефону, телефонуйте батькам за таким номером {phone['Номер телефону']}")

