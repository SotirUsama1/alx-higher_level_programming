#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list = []
    for i in my_list:
        list.append(not i % 2)
    return list
