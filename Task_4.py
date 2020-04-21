# Программа принимает действительное положительное число x и целое отрицательное число
# y . Необходимо выполнить возведение числа x в степень y . Задание необходимо реализовать
# в виде функции my_func(x, y) . При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с
# помощью оператора **. Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.

def my_function(x, y):
    '''Функция возводит x  в степень y'''
    ex = x ** y
    return print(f'{x} в степени {y} равно: {ex}')


my_function(4, -4)

# Или так
'''Функция возводит x  в степень y'''
ex = lambda x, y: x ** y


print(f'x в степени y равно: {ex(4, -4)}')


def my_function_1(x, y):
    '''Функция возводит x  в степень y'''
    alt_x = x
    for i in range(1, abs(y)):
        x = x * alt_x
    ex = 1 / x
    return print(f'x в степени y равно: {ex}')


my_function_1(4, -4)
