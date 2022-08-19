def func_input_data_lower():
    for word in input_data:
        word_lower = word.lower()
        input_data_lower.append(word_lower)


def filter_list():
    for word in input_data_lower:
        if word == word[-1::-1]:
            words.append(word)
        else:
            pass


# Вы в условии когда писали список слов допустили синтаксическую ошибку. не inputdata а input_data^)
input_data = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']
words = []
input_data_lower = []

func_input_data_lower()

result = list(filter(filter_list(), words))
print("Before filter")
print(input_data)
print("-" * 62)
print("After filter")
print(result)
