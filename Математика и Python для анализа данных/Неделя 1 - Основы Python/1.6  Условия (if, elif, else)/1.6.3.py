# Пора объединить полученные знания.
#
# Считайте 1 строку. Она содержит строку с названием типа последующих данных. Возможны 3 типа:
#
# int
# str
# list
# В случае получения другого типа выведите на печать строку "Unknown type".
#
#
# Если получен тип 'int':
#
# Считайте ещё 2 строки. Каждая будет содержать целое число.
#
# Если оба числа равны 0, выведите на печать строку "Empty Ints"
# Иначе выведите на печать сумму этих чисел
#
#
# Если получен тип 'str':
#
# Считайте ещё 1 строку.
#
# Если строка пустая, выведите на печать строку "Empty String"
# Иначе напечатайте эту строку
#
#
# Если получен тип 'list':
#
# Считайте 1 строку и разрежьте её на элементы с помощью split().
#
# Если получившийся список пустой, выведите на печать строку "Empty List"
# Иначе выведите на печать последний элемент списка. Примечание, используйте отрицательный индекс.
# ﻿
#
# Используйте приведение типов для определения пустых списков и строк, а так же чисел, равных 0.
#
# Sample Input 1:
#
# dict
# Sample Output 1:
#
# Unknown type
# Sample Input 2:
#
# int
# 0
# 0
# Sample Output 2:
#
# Empty Ints
# Sample Input 3:
#
# int
# 1
# 2
# Sample Output 3:
#
# 3
# Sample Input 4:
#
# str
# Hello, World!
# Sample Output 4:
#
# Hello, World!
# Sample Input 5:
#
# str
#
# Sample Output 5:
#
# Empty String
# Sample Input 6:
#
# list
# 1 2 3 4 5
# Sample Output 6:
#
# 5
# Sample Input 7:
#
# list
#
# Sample Output 7:
#
# Empty List

t = input()

if t == "int":
    a = int(input())
    b = int(input())
    if a or b:
        print(a + b)
    else:
        print("Empty Ints")
elif t == "str":
    s = input()
    if s:
        print(s)
    else:
        print("Empty String")
elif t == "list":
    lst = input().split()
    if lst:
        print(lst[-1])
    else:
        print("Empty List")
else:
    print("Unknown type")
