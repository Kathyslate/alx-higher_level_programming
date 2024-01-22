#!/usr/bin/python3
def safe_print_list(my_=[], x=0):
    real_x = 0
    for i in range(x):
        try:
            print(my_list[i], end='')
            real_x += 1
        except (IndexError, TypeError):
            break
    print()
    return real_x
