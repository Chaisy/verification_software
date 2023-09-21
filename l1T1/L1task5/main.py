from functions import get_file, get_racsh
if __name__ == '__main__':
    args = get_racsh()

    directory = args[0]
    racshirenie = args[1]

    files = get_file(directory, racshirenie)

    if not files:
        print('We cant find this file.')
    else:
        for file in files:
            print(file)