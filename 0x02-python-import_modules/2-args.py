#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} argument:".format(len(sys.argv)))
    elif len(sys.argv) > 1:
        print("{} arguments:".format(len(sys.argv)))
    else:
        print("0 arguments.")

    if len(sys.argv) >= 1:
        a = 1
        for i in sys.argv:
            print("{}: {}".format(a, i))
            a += 1
