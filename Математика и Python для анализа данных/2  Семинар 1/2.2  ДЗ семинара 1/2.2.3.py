# 3. Список - чётные индексы
# Напишите функцию even_indeces(l), которая будет возвращать только элементы с чётными индексами.
#
#
#
# Примечание. Пример вывода дан для l = [1, 1, 2, 3, 5, 8, 13, 21, 34]
#
# В данной задаче не требуется осуществлять вывод - проверка производится для разных списков!
#
# Sample Input:
#
#
# Sample Output:
#
# [1, 2, 5, 13, 34]

def even_indeces(l):
    return l[::2]
