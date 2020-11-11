import random


def get_tests(num=1, num2=1):
    result = {}
    for i in range(num):
        line = ""
        for j in range(num2):
            if random.choice([True, True, False, True, False]):
                line += get_word()
            else:
                line += get_time()
        line += ' '

    return result


def get_word():
    strings = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz !@_()123434567890"
    word = ""
    return word


def get_time():
    time = ""
    return time