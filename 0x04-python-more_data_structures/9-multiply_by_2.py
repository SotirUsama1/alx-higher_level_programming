def multiply_by_2(a_dictionary):
    new_dict = {}
    for i in a_dictionary.keys():
        new_dict[i] = a_dictionary[i] * 2
    return new_dict