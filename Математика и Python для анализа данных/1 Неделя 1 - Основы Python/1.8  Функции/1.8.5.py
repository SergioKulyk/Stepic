# Напишите функцию convert(L), принимающую на вход список, состоящий из чисел и строк вида:
#
# [1, 2, '3', '4', '5', 6]
# и возвращающую список целых чисел (в том же порядке):
#
# [1, 2, 3, 4, 5, 6]
# Примечание. В этой задаче не нужно ничего считывать и ничего выводить на печать. Только реализовать функцию.

def convert(L):
    return list(map(int, L))

# print(convert([1, 2, '3', '4', '5', 6]))
