#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    list = []
    if idx > 0 and idx < len(my_list) - 1:
        for i in range(len(my_list)):
            if i == idx:
                continue
            list.append(my_list[i])
    return list
