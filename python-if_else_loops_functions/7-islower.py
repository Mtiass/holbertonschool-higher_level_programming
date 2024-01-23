#!/usr/bin/python3
def islower(c):
    if not c:
        return False
    else:
        for i in range(97, 123):
            if chr(i) == c:
                return True
            else:
                continue
        return False
