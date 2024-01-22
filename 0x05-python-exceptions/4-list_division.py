#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if len(my_list_1) < list_length or len(my_list_2) < list_length:
        print("out of range")
        return [None] * list_length

    result = [None] * list_length
    for i in range(list_length):
        try:
            if not (isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float))):
                print("wrong type")
                result[i] = 0
                continue
            result[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result[i] = 0

    return result
