# Площадь ромба
#
#
# Даны длины 2 диагоналей ромба (каждая с новой строки).
# Значения могут быть дробными.
#
# Найдите площадь ромба S. В качестве ответа запишите (каждое с новой строки) следующие значения:
# S, приведённое к целочисленному типу
# S, округлённое до 1 знака после запятой с помощью функции  round()
# S, точное значение без округления
# Площадь ромба можно найти на wiki.
#
# Sample Input 1:
#
# 2
# 10
# Sample Output 1:
#
# 10
# 10.0
# 10.0
# Sample Input 2:
#
# 3.6
# 7.6
# Sample Output 2:
#
# 13
# 13.7
# 13.68

d1 = float(input())
d2 = float(input())

S = (d1 * d2) / 2.

print(int(S))
print(round(S, 1))
print(S)
