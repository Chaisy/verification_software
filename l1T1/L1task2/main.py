from functions import check, check_age, sort_age
from functions import Person


if __name__ == '__main__':
    #создаем массив для людей
    massiv = []

    # вводим до введенного '-'
    print("If you enter smth wrong? loop was ended!!!")
    while True:
        name = check_name(input('First name: '))
        surname = check_name(input('Last name: '))
        age = check_age(input('Age: '))

        massiv.append(Person(name, surname, age))

        stop = input('Enter \'-\' if you want to stop ')
        if stop == '-':
            break

    # вывод массива через итерирование по коллекции
    print('\n' + '\n'.join(f'{a.last_name} {a.first_name} {a.age}'
                                        for a in massiv))

    # при помощи функии получаем сортировку возрастов
    ages = sort_age(massiv)
    print("Age: ")
    print(f'\nmin: {ages[0]}\nmax:  {ages[1]}\naverage: {ages[2]}')