#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    j = len(sys.argv) - 1
    if j == 1:
        print("{} argument:".format(j))
    elif j == 0:
        print("{} arguments.".format(j))
    else:
        print("{} arguments:".format(j))

    if j >= 1:
        a = 1
        for i in sys.argv:
            print("{}: {}".format(a, i))
            a += 1
