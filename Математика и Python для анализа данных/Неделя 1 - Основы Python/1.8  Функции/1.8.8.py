# Напишите функцию maxId(L), принимающую на вход список чисел и строк вида:
#
# [1, 2, '42', '3', '4', '5', 6, 13]
# без повторений, и находящую индекс максимального целого числа в списке.
#
# Используйте ранее написанную функцию convert(L).
#
#
#
# Примечание. В этой задаче не нужно ничего считывать и ничего выводить на печать. Только реализовать функцию.
#
# Sample Input 1:
#
# [1, 2, '42', '3', '4', '5', 6, 13]
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# ['0', 1, 2, '3', '4', '5', 6, '666', 42]
# Sample Output 2:
#
# 7

def convert(L):
    return list(map(int, L))

def maxId(L):
    L = convert(L)
    return L.index(max(L))
