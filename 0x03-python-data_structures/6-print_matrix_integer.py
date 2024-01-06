#!/usr/bin/python3
def print_matrix_integer(matrix=[[0]]):
    max_length = 0
    for row in matrix:
        for num in row:
            length = len(str(num))
            if length > max_length:
                max_length = length

    format_string = "{:>" + str(max_length) + "} "

    for row in matrix:
        line = ""
        for num in row:
            line += format_string.format(num)
        print(line)
