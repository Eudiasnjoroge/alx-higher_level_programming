#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for item in range(x):
            print("{}".forma(my_list[item], end='')
            num += 1
    except IndexError:
        pass
    print()
    return num
