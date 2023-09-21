import sys

#проверяем правильность введенных параметров, чтобы они были больше 0
def check_hw(num):
    try:
        number = float(num)
        if number > 0: return num
        else:
            raise ValueError('Error!')
    except ValueError as e:
        print(f'Error: {e}')
        exit(-1)


# get arguments with checking if they are valid
def get_hw():
    #возвращает список параметров командной строки, передаваемых скрипту
    if len(sys.argv) != 3:
        print('Example:\n py main.py <length> <width>')
        exit(-1)

    a = check_hw(sys.argv[1])
    b = check_hw(sys.argv[2])

    return a, b


def get_square(h, w):
    return h * w