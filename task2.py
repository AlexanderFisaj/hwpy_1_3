# Задача 2. В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

fruits_list = ['абрикос', 'авокадо', 'апельсин', 'айва', 'яблоко', 'банан', 'вишня', 'киви', 'лимон', 'манго', 'груша']
letter_selection = input("Введите букву: ").lower()
my_fruits_list = []

for fruit in fruits_list:
    if fruit[0] == letter_selection:
        my_fruits_list.append(fruit)

if not my_fruits_list:
    print(f'Фруктов, начинающихся на букву "{letter_selection}" нет')
else:
    print(", ".join(my_fruits_list))
