input_data = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']

result = list(filter(lambda item: item.lower() == item[-1::-1].lower(), input_data))

print(input_data)
print(result)
