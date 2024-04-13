#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None: return None
    my_list = [(k, a_dictionary.get(k)) for k in a_dictionary.keys()]
    best_s = my_list[1][1]
    best_k = ""
    for i in my_list:
        if i[1] > best_s:
            best_s = i[1]
            best_k = i[1]
    return best_k
