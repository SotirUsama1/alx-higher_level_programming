#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None: return None
    my_list = [(k, a_dictionary.get(k)) for k in a_dictionary.keys()]
    best_s = 0
    best_k = ""
    for i in my_list:
        if i[1] > best_s:
            best_s = i[1]
            best_k = i[0]
    return best_k

my_dict = { 'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Moll': 16 }
best_key = best_score(my_dict)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))