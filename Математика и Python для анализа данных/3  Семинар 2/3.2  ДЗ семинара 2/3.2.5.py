# 4. Скопировать многомерный список без deepcopy

# На вход подаётся многоуровневый список L1 вида:
#
# L1 = [['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]
# Не используя метод deepcopy скопируйте всё содержимое списка L1 в L2.
# Учтите, что элементы дочерних элементов L1 после этого будут изменены и эти изменения не должны отразиться на L2.
# Т.е. сделайте по настоящему глубокую копию.
#
# Принимаем список может иметь произвольное число дочерних списков
# Длинны дочерних списков могут быть произвольными (дочерний список может не содержать элементов) и не равны друг другу
# Элементы дочерних списков могут повторяться
# Порядок в получившемся списке не важен
#
#
# Примечание1. В этой задаче не надо ничего считывать или выводить на печать.
#
#
# Примечание2. Тип переменной можно узнать с помощью type() и сравнить с типом list:
#
# type(elem) is list   # Вернёт True для списков и False для всех остальных
# Примечание3. Deepcopy использовать нельзя

L1 = [['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]

def list_copy(L1, L2):
    while

L2 = []
L2 = list_copy(L1, L2)
print(L1)
print(L2)

print("*"*100)
L1[2][1][1][0][0][0][0] = 3

print(L1)
print(L2)