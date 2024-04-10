#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    common = set_1 & set_2
    uni = set_1.union(set_2)
    unq = []
    for i in uni:
        for j in common:
            if i == j:
                break
            unq.append(i)
    return set(unq)
