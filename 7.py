def check_list(my_list, my_dict):
    for item in my_list:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1


list_of_number = [1, 13, 83, 1, 22, 31, 83, 99, 1, 13, 1, 22, 1, 13]
dict_of_number = {}

check_list(list_of_number, dict_of_number)

print(f"list of number: {list_of_number}")
print("-" * 67)
print(f"dict of number: {dict_of_number}")
