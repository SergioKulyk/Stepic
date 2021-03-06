# Додекаэдр
#
# На вход программа получает 1 строку - длину ребра додекаэдра.
# Используя формулы из Wiki найдите площадь поверхности и объём фигуры.
# Ответ округлите до 2 знака после запятой.
# Sample Input 1:
#
# 1
# Sample Output 1:
#
# 20.65
# 7.66
# Sample Input 2:
#
# 2
# Sample Output 2:
#
# 82.58
# 61.3

a = int(input())
S = 3*a**2*((5*(5+2*5**0.5))**0.5)
V = a**3/4*(15+7*5**0.5)
print(round(S, 2))
print(round(V, 2))
