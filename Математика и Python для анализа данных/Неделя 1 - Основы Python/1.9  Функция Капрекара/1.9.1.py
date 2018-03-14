# numerics(n)

# Напишите функцию numerics(n), принимающую на вход 1 натуральное 4х значное число, а возвращающую список цифр из которых состоит число.
#
# Если какая-то цифра встречается в исходном числе несколько раз, то и в ответе она должна встретиться несколько раз (это критично, т.к. потом мы будем составлять из этих цифр снова 4х значные числа). Порядок цифр в ответе не важен.
#
#
#
# Примечание. В этой задаче не нужно ничего считывать и ничего выводить на печать. Только реализовать функцию.
#
# Sample Input 1:
#
# 3412
# Sample Output 1:
#
# [2, 1, 4, 3]
# Sample Input 2:
#
# 4224
# Sample Output 2:
#
# [4, 2, 2, 4]

def numerics(n):
    return list(map(int, list(str(n))))
