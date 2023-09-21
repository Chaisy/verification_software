import os
import sys
import requests
import validators
import subprocess
import re


# скачивваем по юрл в папку
def saving(url, dir, active):
    try:
        # отправлем запрос на получение по юрл
        response = requests.get(url)
#удачное получение
        if response.status_code == 200:
            file_name = os.path.basename(url)

            # удаляем все параметры
            file_name = re.sub(r'[?&].+', '', file_name)

            file_path = os.path.join(dir, file_name)

            # записываем бинарно
            with open(file_path, 'wb') as file:
                file.write(response.content)

            if active:
                subprocess.Popen(["start", file_path], shell=True)
        else:
            print(f'Error, status code = {response.status_code}')
            exit(-1)
    except Exception as e:
        print(f'Error: {str(e)}')
        exit(-1)


# получаем аргументы если они валидны
def get_param():
    # "url" for &, Windows powershell doesn't process it
    if len(sys.argv) != 3:
        print('Example:\n'
              'py main.py "<url>" <directory>')
        exit(-1)

    url = check_url(sys.argv[1])
    check_dir(sys.argv[2])

    return url, sys.argv[2]


# check if url is valid
def check_url(url):
    try:
        if not url.startswith('"') or not url.endswith('"'):
            raise ValueError('Error!')

        # delete ""
        url_ = url[1: len(url) - 1]

        if not validators.url(url_):
            raise ValueError('Error!')

        return url_
    except ValueError as e:
        print(f'Error: {e}')
        exit(-1)


# check if directory is valid
def check_dir(directory):
    try:
        if not os.path.isdir(directory):
            raise ValueError('Error!')
        if not os.path.exists(directory):
            raise ValueError(f'{directory} does not exist')
    except ValueError as e:
        print(f'Error: {e}')
        exit(-1)