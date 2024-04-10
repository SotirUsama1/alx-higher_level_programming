#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordKeys = sorted(a_dictionary.keys())
    for i in ordKeys:
        print("{}: {}".format(i, a_dictionary.get(i)))
