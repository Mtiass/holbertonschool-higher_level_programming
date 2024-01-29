#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dict = dict(a_dictionary)
    for i in b_dict:
        b_dict[i] *= 2
    return (b_dict)
