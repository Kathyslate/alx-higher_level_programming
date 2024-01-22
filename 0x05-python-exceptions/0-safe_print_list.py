#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print_count = 0
    error_element = None

    try:
        for element in my_list[:x]:
            print(element, end='')
            print_count += 1
    except TypeError:
        error_element = my_list[0] if my_list else None
        return print_count

    print()
    return print_count
