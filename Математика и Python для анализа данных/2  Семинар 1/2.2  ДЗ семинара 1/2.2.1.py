# 1. Предел функции
# Реализуйте функцию f(x):
#
# f(x)=2arctg(x)
#
# Найдите предел функции (ответ округлите до 3 знака после запятой) при x→+∞
#
# limx→+∞2arctg(x)
# Hint: Арктангенс доступен в модуле math под именем atan.
#
# Sample Input:
#
#
# Sample Output:
#
# 3.142

import math

def f(x):
    return 2 * math.atan(x)

lim = f(100_000)
print(round(lim, 3))

