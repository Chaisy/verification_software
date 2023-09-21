import re

#объявляем класс для человека и его возраста
class Person:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age
# проверяем корректность введенных данных для имени и фамилии(с большой буквы и более 2 символов)
def check(str):
    try:
        if re.match(r'^[A-Z][a-z]+', str): return str(str)
        else: raise ValueError('Error!')
    except ValueError as e:
        print(f'Error: {e}')
        exit(-1)


# валидность возраста  в промежутке 0-100
def check_age(age):
    try:
        if re.match(r'^[0-9]+', age) and 0 <= int(age) <= 100: return int(age)
        else: raise ValueError('Error!')
    except ValueError as e:
        print(f'Error: {e}')
        exit(-1)


# считаем средний возраст, минимальный и максимальный
def sort_age(massiv):
    ages = [m.age for m in massiv]

    mini = min(person.age for person in massiv)
    maxi = max(person.age for person in massiv)
    average = sum(person.age for person in massiv) / len(ages)
#возвращаем минимальное, максимальное и округление до 2ч знаков
    return mini, maxi, round(average,2)


