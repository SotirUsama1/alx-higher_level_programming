#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    argc = len(args)
    match argc:
        case 1:
            print("0 arguments.")
        case 2:
            print("1 argument:")
            print("1: {}".format(args[1]))
        case _:
            print("{} arguments:".format(argc))
            for i in range(1, argc):
                print("{}: {} ".format(i, args[i]))
