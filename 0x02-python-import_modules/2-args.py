#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = 1
    if len(sys.argv) >= 1:
        print("{} arguments:".format(len(sys.argv)))
        for i in sys.argv:
            print("{}: {}".format(a, i))
            a += 1
    else:
        print("arguments.")
