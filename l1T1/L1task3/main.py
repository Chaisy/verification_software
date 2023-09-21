from functions import get_hw, get_square

if __name__ == '__main__':
    hw = get_hw()

    h = hw[0]
    w = hw[1]

    S = get_square(h, w)
    print(f"{h}*{w} = {S}")