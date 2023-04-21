# Задача 1. Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

number = int(input("Введите количество элементов последовательности Фибоначчи: "))
n_fib_sequence = [1, 1]
if number == 1:
    n_fib_sequence = 1
elif number > 2:
    for i in range(2, number):
        n_fib_sequence.append(n_fib_sequence[i - 1] + n_fib_sequence[i - 2])
print(*n_fib_sequence)