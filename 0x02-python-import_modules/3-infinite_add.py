#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = argv
    argc = len(args)
    sum = 0
    for i in range(1, argc):
        sum = sum + int(args[i])
    print(sum)

