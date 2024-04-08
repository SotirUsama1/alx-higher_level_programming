'''
#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = argv
    argc = len(args)
    sum = 0
    for i in range(1, argc):
        sum = sum + int(args[i])
    print(sum)
'''

#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))