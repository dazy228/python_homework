text = (input("Введите предложени из слов: "))        # В данном случае я ввожу слова: good night
splitted_text = text.split()
# print(splitted_text)
first_word = splitted_text[0].title()
second_word = splitted_text[1].upper()
# print(first_word, second_word)
reverse_text_1 = f"!{second_word} {first_word}?"
reverse_text_2 = "!{a} {b}?".format(a=second_word, b=first_word)
reverse_text_3 = "!{0} {1}?".format(second_word, first_word)
new_file = open("splitted_file.txt", "w")
print(text, reverse_text_1, reverse_text_2, reverse_text_3, sep="<<<>>>", file=new_file)
new_file.close()
