#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list)
    if idx < 0:
        return "none"
    elif idx >= size:
        return "none"
    else:
        return my_list[idx]
