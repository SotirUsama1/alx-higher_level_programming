#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    argc = len(args)
    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:")
        print("1: {}".format(args[1]))
    else:
        print("{} arguments:".format(argc - 1))
        for i in range(1, argc):
           print("{}: {} ".format(i, args[i]))
