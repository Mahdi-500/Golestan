import time
import os
def length(number, length) -> bool:
    flag = True
    if len(number) != length:
        flag = False
    return flag

def just_str(x) -> bool:
    flag = True
    if str(x).isalpha() == False:
        flag = False
    return flag

def just_number(id) -> bool:
    flag = True
    if str(id).isdigit() == False:
        flag = False
    return flag

def str_int(x) -> bool:
    flag = True
    if str(x).isalnum() == False:
        flag = False
    return flag

def try_except(var_name, text) -> bool and str or int:
    flag = False
    try:
        var_name = input(text)
    except KeyboardInterrupt or EOFError:
        flag = True
        return flag, 0
    else:
        return flag, var_name

def action(text) -> None:
    print('\n' + text)
    time.sleep(3)
    os.system('cls')
