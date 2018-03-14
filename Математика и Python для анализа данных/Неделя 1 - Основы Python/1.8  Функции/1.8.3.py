# Напишите функцию, для нахождения двойного факториала числа dfactorial(n).
#
# Двойной факториал числа n обозначается n‼ и определяется как произведение всех натуральных чисел в отрезке [1,n],
# имеющих ту же чётность, что и n.
#
# Для чётного n:
# Для нечётного n:

def dfactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * dfactorial(n - 2)

# print(dfactorial(0))  # 1
# print(dfactorial(1))  # 1
# print(dfactorial(2))  # 2
# print(dfactorial(3))  # 3
# print(dfactorial(4))  # 8
# print(dfactorial(5))  # 15
