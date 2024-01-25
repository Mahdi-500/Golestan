import time
import os


def length(number, length) -> bool:
    flag = False
    if len(number) != length:
        flag = True
    return flag


# check's if it's string


def just_str(x) -> bool:
    flag = False
    if str(x).isalpha() == False:
        flag = True
    return flag


# check's if it's number


def just_number(id) -> bool:
    flag = False
    if str(id).isdigit() == False:
        flag = True
    return flag


# check's if it's just string and number


def str_int(x) -> bool:
    flag = False
    if str(x).isalnum() == False:
        flag = True
    return flag


# exception handling


def try_except(var_name, text) -> bool and str or int:
    flag = False
    try:
        var_name = input(text)
    except KeyboardInterrupt or EOFError or ValueError:
        flag = True
        return flag, 0
    else:
        return flag, var_name


def message(text) -> None:
    print("\n" + text)
    time.sleep(3)
    os.system("cls")
