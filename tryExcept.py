import random


def hello():
    state = True
    while state:
        name = input("Please input your name:")
        if name == "q":
            state = False
            continue
        try:
            age = int(input("Please input your age:"))
            print(f"{name},you are {age}-years-old\nIf you want to quit,press 'q'")
        except ValueError:
            print('Please input a number,try again!')


def cat(txt: str):
    try:
        txt_str = open(txt, encoding='utf-8').read()
        print(txt_str)
    except FileNotFoundError:
        print('file not found')


def print45():
    a_dig = []
    a_div = []
    for i in range(18):
        # print(int(2 * random.random()) + 4)
        a = random.random()
        if a < 0.6:
            a_dig.append(5)
            print(5)
        else:
            print(4)
            a_dig.append(4)
        try:
            a_div.append(a_dig.count(5) / a_dig.count(4))
        except ZeroDivisionError:
            a_div.append(0)

        print('count', a_dig.count(5), a_dig.count(4))
    print("5.count/4.count 5 4 的计数为:", a_div, a_dig.count(5), a_dig.count(4))


if __name__ == '__main__':
    print45()
