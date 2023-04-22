# Задача 3. 
# Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». 
# Если фраза ему неизвестна, он выводит соответствующую фразу.

import os

print('Бот запущен. Для прекращения общения с ботом введите ":q" и подтвердите ввод <Enter>!')

with open('E:\GB\Python\hwpy_1_3\dict_bot.txt', 'r', encoding='utf-8') as file_dict:
    dictionary = eval(file_dict.read())    

flag = True

while flag:
    phrase = input('Введите вопрос: ')
    
    if phrase == ":q":
        file_dict.close()
        flag = False
    else:
        answer_bot = dictionary.get(phrase)
    if answer_bot:
        print(answer_bot)
    else:
        new_answer = input('Я не знаю ответа. Как мне ответить на этот вопрос? ')
        dictionary[phrase] = new_answer
        with open('E:\GB\Python\hwpy_1_3\dict_bot.txt', 'w', encoding='utf-8') as file_dict:
            file_dict.write(str(dictionary))