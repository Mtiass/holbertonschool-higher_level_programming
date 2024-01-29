#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = set(my_list)
    newlist = list(newlist)
    result = 0
    for i in range(len(newlist)):
        result += newlist[i]
    return (result)
