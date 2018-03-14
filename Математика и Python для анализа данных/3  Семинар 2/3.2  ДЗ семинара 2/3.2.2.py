# 1.2 Предел функции
# Найдите предел функции f(x)=sin(πx2)x при x→+∞
#
# Ответ округлите до 3 знака после запятой.
from math import sin, pi

def f(x):
    return sin(pi * x / 2) / x

x = 10e6
print(round(f(x), 3))
