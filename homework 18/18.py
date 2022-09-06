import csv
import openpyxl

wb = openpyxl.Workbook()

sheet = wb['Sheet']

list_of_file_0 = ['', 'Person 1', 'Person 2', 'Person 3', 'Person 4', 'Person 5', 'Person 6']
list_of_file_1 = []
list_of_file_2 = []
list_of_file_3 = []
list_of_file_4 = []

with open('task.csv', encoding='utf-8') as file:
    file_reader = csv.reader(file)
    for row in file_reader:
        # print(f'{row[0]} |  {row[1]} |  {row[2]} |  {row[3]}')
        list_of_file_1.append(row[0])
        list_of_file_2.append(row[1])
        list_of_file_3.append(row[2])
        list_of_file_4.append(row[3])

    for row_index, row in enumerate((list_of_file_0, list_of_file_1, list_of_file_2, list_of_file_3, list_of_file_4)):
        for col_index, value in enumerate(row):
            cell = sheet.cell(row=row_index+1, column=col_index+1)
            cell.value = value

wb.save('task_02.xlsx')