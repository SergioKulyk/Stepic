# Шаг 7 - Вытянуть двумерный список
# Дан двумерный список L1 (список списков) вида:
#
# L1 = [['one', 'two', 'three'], [1, 2, 3, 4, 5, 6]]
# Сохраните в список L2 все элементы дочерних списков L1 (т.е. вытяните их в 1 цепочку) вида:
# ['one', 'two', 'three', 1, 2, 3, 4, 5, 6]
# L1 может иметь произвольное число дочерних списков
# Длины дочерних списков могут быть произвольными (дочерний список может не содержать элементов) и не равны друг другу
# Элементы дочерних списков могут повторяться
# Порядок в получившемся списке L2 не важен
#
#
# Примечание. В этой задаче не надо ничего считывать или выводить на печать.
# Все необходимые данные находятся в L1, а сохранить их надо в L2.

L1 = [['one', 'two', 'three'], [1, 2, 3, 4, 5, 6]]
L2=[]

for i in L1:
    for j in i:
        L2.append(j)
