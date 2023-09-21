import os
import sys
import re


# main function which finds all files with extension
def get_file(directory, racshirenie):
    result = []

    # проходимя по всему и ищем нужный нам файл
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(racshirenie):
                result.append(os.path.join(root, file))

    return result


# проверяем валидность аргументов
def get_racsh():
    if len(sys.argv) != 3:
        print('Example:\n'
              'py main.py <directory> <racshirenie>')
        exit(-1)

    check_dir(sys.argv[1])
    check_racsh(sys.argv[2])

    return sys.argv[1], sys.argv[2]


# проверяем папку на валидность
def check_dir(directory):
    try:
        if not os.path.isdir(directory):
            raise ValueError('Error!')
        if not os.path.exists(directory):
            raise ValueError(f'{directory} does not exist')
    except ValueError as e:
        print(f'Error: {e}')
        exit(-1)


# проверяем расширение на валидность нужно: .cpp, .py, .txt etc..
def check_racsh(extension):
    try:
        if not re.match(r'^\..+', extension):
            raise ValueError('Error!')
    except ValueError as e:
        print(f'Error: {e}')
        exit(-1)