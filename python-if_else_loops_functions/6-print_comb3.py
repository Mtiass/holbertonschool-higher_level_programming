#!/usr/bin/python3
for i in range(0,10):
    for c in range(i + 1, 10):
        if i != c:
            print("{}{}".format(i, c), end=", " if i != 8 or c != 9 else '\n')
