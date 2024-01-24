#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    total = 0
    if len(sys.argv) > 0:
        for i in arguments:
            total += int(i)
        print(total)
    else:
        print(total)
