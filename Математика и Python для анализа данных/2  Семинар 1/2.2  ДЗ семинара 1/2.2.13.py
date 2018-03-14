# C. fix_start

# Считайте строку.
#
# Напишите функцию, принимающую на вход строку, находящую 1й символ и заменяющую все его вхождения в строку кроме 1 на *.
#
# Выведите на печать результат работы вашей функции, применённый к считанной строке.
#
#
#
# Hint: у строк есть метод replace(old, new)
#
# Sample Input 1:
#
# babble
# Sample Output 1:
#
# ba**le
# Sample Input 2:
#
# aabirvalg
# Sample Output 2:
#
# a*birv*lg
# Sample Input 3:
#
# donut
# Sample Output 3:
#
# donut

def fix_start(s):
    return s[0] + s[1:].replace(s[0], '*')

s = input()
print(fix_start(s))
