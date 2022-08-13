old_dictionary = {"a": 29, "b": 63, "c": 18, "d": 21, "e": 54}


def dict_swap():
    new_dictionary = {value: key for key, value in old_dictionary.items()}
    return new_dictionary


print(dict_swap())


