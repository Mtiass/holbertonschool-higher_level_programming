#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printel = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end='')
            printel += 1
        except IndexError:
            break
    print()
    return (printel)
