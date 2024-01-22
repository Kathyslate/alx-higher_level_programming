#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            if i < len(my_list):
                print(my_list[i], end=' ')
                count += 1
            elif i >= len(my_list) and my_list:
                print(my_list[-1], end=' ')
                count += 1
        print()
        return count
    except (TypeError, IndexError):
        print("Error: List must contain only printable elements")
        return 0
