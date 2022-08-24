def analysis(your_list, your_dict):
    for item in your_list:
        if item in your_dict:
            your_dict[item] += 1
        else:
            your_dict[item] = 1


my_list = [1, 13, 83, 1, 22, 31, 83, 99, 1, 13, 1, 22, 1, 13]
my_dict = {}
print(f"list of numbers {my_list}")
print("-" * 69)
analysis(my_list, my_dict)
print(f"repeating number dictionary {my_dict}")