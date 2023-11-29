#!/usr/bin/python3
def uppercase(str):
    temp = ""
    for i in str:
        if order >= 97 and order <= 122:
            temp += chr(ord(i) - 32)
        else:
            temp += i
    print("{}".format(temp))
