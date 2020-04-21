# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии
# Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
# добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких
# чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого
# завершить программу.

key = None
summ_1 = [0]

while key == None or key == 0:
    user_numbers = str(
        input('Веведите сколько угодно чисел разделяя их пробелом, для выхода из программы введите * : ')).split()
    key = user_numbers.count('*')

    if key == 0:
        for i in range(0, len(user_numbers)):
            user_numbers[i] = int(user_numbers[i])
        summ = sum(user_numbers)
        print(f'Сумма чисел равна: {summ}')
        summ = sum(user_numbers) + sum(summ_1)
        del summ_1[0]
        summ_1.append(summ)
        if sum(summ_1) > 0:
            print(f'Сумма сумм чисел равна: {summ}')
    else:
        user_numbers[-1] = '0'
        for i in range(0, len(user_numbers)):
            user_numbers[i] = int(user_numbers[i])
        if sum(user_numbers) == 0:
            summ = sum(user_numbers) + sum(summ_1)
            print(f'Итоговая сумма равна: {summ}')
        else:
            summ = sum(user_numbers) + sum(summ_1)
            print(f'Итоговая сумма равна: {summ}')
        break
