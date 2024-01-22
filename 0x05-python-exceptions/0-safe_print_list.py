#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print_count = 0
    error_element = None

    try:
        for element in my_list:
            if print_count < x:
                print(element, end=' ')
                print_count += 1
            else:
                break
    except TypeError:
        print("Error: List contains non-printable type '{}'.".format(error_element))
        return 0

    print() # newline after all elements are printed
    return print_count
