# Реализовать функцию my_func() , которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.

def two_max_number(number_1, number_2, number_3):
    '''Функция принимает три числа и возвращает сумму наибольших двух аргументов'''
    summ = sum([number_1, number_2, number_3]) - min([number_1, number_2, number_3])
    return print(f'Сумма двух наибольших чисел: {summ}')


two_max_number(3, 5, -1)

# Или так
'''Функция принимает три числа и возвращает сумму наибольших двух аргументов'''
summ = lambda number_1, number_2, number_3: sum([number_1, number_2, number_3]) - min([number_1, number_2, number_3])


print(f'Сумма двух наибольших чисел: {summ(3, 5, -1)}')
