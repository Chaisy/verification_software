from random import randint


def getText():
    #возвращаем строку с числом, которое получаем при помощи randint
    return f"Hello, world!\nAndhiagain!\n" + f"{'!' * randint(5, 50)}"
