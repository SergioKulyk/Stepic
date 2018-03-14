# Напишите 2 функции:
# для нахождения факториала числа factorial(n) - n!=1⋅2⋅3⋅…⋅n
# для нахождения суперфакториала числа sf(n) - sf(4)=1!⋅2!⋅3!⋅…⋅n!
# Используйте функцию факториала для вычисления суперфакториала, чтобы сократить объём кода.
#
# Примечание. В этой задаче не нужно ничего считывать и ничего выводить на печать. Только реализовать функцию.
# Sample Input 1:
#
# 0
# Sample Output 1:
#
# 1 1
# Sample Input 2:
#
# 1
# Sample Output 2:
#
# 1 1
# Sample Input 3:
#
# 2
# Sample Output 3:
#
# 2 2
# Sample Input 4:
#
# 3
# Sample Output 4:
#
# 6 12
# Sample Input 5:
#
# 4
# Sample Output 5:
#
# 24 288
# Sample Input 6:
#
# 5
# Sample Output 6:
#
# 120 34560

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sf(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n) * sf(n - 1)
