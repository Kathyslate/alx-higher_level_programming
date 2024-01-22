#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x < 0:
        raise ValueError("x should be greater than or equal to 0")

    real_x = 0
    for i in range(x):
        try:
            print(my_list[i], end=' ')
            real_x += 1
        except (IndexError, TypeError):
            break
    print()
    return real_x
