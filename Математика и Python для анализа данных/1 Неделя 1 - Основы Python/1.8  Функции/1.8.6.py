# Напишите функцию перевода числа из десятичной системы счисления в систему с основанием n
#
# Функция translate должна принимать 2 параметра:
#
# обязательный (исходное целое число в десятичной системе счисления)
# необязательный, по-умолчанию 2 (основание новой системы счисления, в которую переводится число)
# Примечание 1. Все новые системы счисления имеют основание меньше 10
#
# Примечание 2. В этой задаче не нужно ничего считывать и ничего выводить на печать. Только реализовать функцию.
#
#
#
#
#
# Для перевода из привычной нам десятичной системы исчисления в систему по основанию n, необходимо:
#
# разделить исходное число на n
# записать остаток от деления (шаг 1)
# для результата деления (шаг 1) повторить операцию с шага 1
# если результат деления равен 0, прекратить операцию
# Составить число в новой системе счисления из остатков (от последнего вычисленного к первому)
# На примере перевода из десятичной системы в двоичную:
#
# Допустим, нам нужно перевести число 19 в двоичное. Вы можете воспользоваться следующей процедурой :
#
# 19 /2 = 9 с остатком 1
# 9 /2 = 4 c остатком 1
# 4 /2 = 2 без остатка 0
# 2 /2 = 1 без остатка 0
# 1 /2 = 0 с остатком 1
#
# Итак, мы делим каждое частное на 2 и записываем остаток в конец двоичной записи.
# Продолжаем деление до тех пор, пока в частном не будет 0. Результат записываем справа налево.
# То есть нижняя цифра (1) будет самой левой и т.д. В результате получаем число 19 в двоичной записи: 10011.
#
#
# Sample Input 1:
#
# 19
# Sample Output 1:
#
# 10011
# Sample Input 2:
#
# 19 7
# Sample Output 2:
#
# 25
# Sample Input 3:
#
# 10 2
# Sample Output 3:
#
# 1010
# Sample Input 4:
#
# 8 3
# Sample Output 4:
#
# 22

def translate(n, s=2):
    res = ""
    while n != 0:
        res += str(int(n % s))
        n = int(n / s)
    return res[::-1]


# print(translate(10))  # 1010
# print(translate(10, 3))  # 101
# print(translate(10, 4))  # 22
# print(translate(10, 5))  # 20
# print(translate(10, 6))  # 14
# print(translate(10, 7))  # 13
# print(translate(10, 8))  # 12
# print(translate(10, 9))  # 11
# print(translate(10, 10))  # 10
