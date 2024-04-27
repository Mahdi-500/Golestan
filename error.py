import time
import os
import pandas as pd

def length(number, length) -> bool:
    flag = False
    if len(number) != length:
        flag = True
    return flag


def just_str(x) -> bool:  # todo - check's if it's string
    flag = False
    if str(x).isalpha() == False:
        flag = True
    return flag


def just_number(id) -> bool:  # todo - check's if it's number
    flag = False
    if str(id).isdigit() == False:
        flag = True
    return flag


def str_int(x) -> bool:  # todo - check's if it's just string and number
    flag = False
    if str(x).isalnum() == False:
        flag = True
    return flag


def try_except(var_name, text) -> bool and str or int:  # todo - exception handling
    flag = False
    try:
        var_name = input(text)
    except KeyboardInterrupt or EOFError or ValueError:
        flag = True
        return flag, 0
    else:
        return flag, var_name


def try_except_pd(path) -> bool:  # todo - exception handeling for pandas
    flag = False
    
    try:
        pd.read_csv(path)
    except pd.errors.EmptyDataError or FileNotFoundError:
        flag = True

    return flag

def message(text) -> None:
    print("\n" + text)
    time.sleep(5)
    os.system("cls")
