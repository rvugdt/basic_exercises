# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

def gender_count(school: list, is_male: dict) -> dict:
    class_data = {}
    for klass in school:
        class_name = klass['class']
        students = klass['students']
        girls_count = 0
        boys_count = 0
        for student in students:
            first_name = student['first_name']
            if first_name in is_male and is_male[first_name]:
                boys_count+=1
            elif first_name in is_male and not is_male[first_name]:
                girls_count+=1
        class_data[class_name]={'девочек': girls_count, 'мальчиков': boys_count}
    return class_data

def name_retries(students: list) -> dict:
    name_counts = {}

    for student in students:
        name = student['first_name']
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1
    
    return name_counts

def most_often_name(students: list) -> str:
    name_counts = name_retries(students)
    for name in name_counts.keys():
        if name_counts[name] == max(name_counts.values()):
            return name

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
name_counts = name_retries(students)
for name, count in name_counts.items():
    print(f'{name}: {count}')



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
print(f'\nСамое частое имя среди учеников: {most_often_name(students)}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
print()
for klass, stud_list in enumerate(school_students):
    print(f'Самое частое имя в классе {klass+1}: {most_often_name(stud_list)}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
genders = gender_count(school, is_male)
print()
for class_name, counts in genders.items():
    print(f'Класс {class_name}: девочек {counts["девочек"]}, мальчиков {counts["мальчиков"]}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
genders = gender_count(school, is_male)
print()
for class_name, gndrs in genders.items():
    for gendr, val in gndrs.items():
        if val == max(gndrs.values()):
            print(f'Больше всего {gendr} в классе {class_name}')