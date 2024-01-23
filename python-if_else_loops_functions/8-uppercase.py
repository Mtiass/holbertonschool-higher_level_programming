#!/usr/bin/python3
def uppercase(str):
    empty = ""
    for ch in str:
        if ch >= 'a' and ch <= 'z':
            empty += chr(ord(ch) - 32)
        else:
            empty += ch
    print(empty)
