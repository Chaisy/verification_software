from functions import get_param, saving

if __name__ == "__main__":
    args = get_param()

    url = args[0]
    dir = args[1]

    download(url, dir, True)