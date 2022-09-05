import json
import csv
import random


def create_a_phone():
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    third = {3: random.randint(0, 9),
             4: [5, 7, 9][random.randint(0, 2)],
             5: [i for i in range(10) if i != 4][random.randint(0, 8)],
             7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
             8: random.randint(0, 9), }[second]

    suffix = random.randint(999999, 10000000)
    # print(second)
    # print(third)
    # print(suffix)
    return "+3{}{}{}".format(second, third, suffix)


# print(create_a_phone())

output_data_zero = []
with open('dict.json') as f:
    output_data = json.load(f)

# print(type(output_data))

output_data_csv_zero = []
first_row = ['Key', 'Name', 'Age', 'Phone number']


with open('task.csv', mode='w', encoding='utf-8', newline='') as file:
    output_data_csv = csv.DictWriter(file, fieldnames=first_row)
    output_data_csv.writeheader()
    for item, value in output_data.items():
        output_data_csv.writerow({'Key': item, 'Name': value[0], 'Age': value[1], 'Phone number': create_a_phone()})
