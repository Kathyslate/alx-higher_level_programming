#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_tuple = ()
    
    for i in range(2):
        try:
            a = tuple_a[i]
        except IndexError:
            a = 0
            
        try:
            b = tuple_b[i]
        except IndexError:
            b = 0
            
        sum_tuple += (a + b,)
        
    return sum_tuple
