# sum()

# Функция sum() принимает на вход массив(любого типа) чисел и находит их сумму:
#
# Image: https://ucarecdn.com/53e9cdd2-ea5f-455d-9966-cf3a03b0ce22/
# Считайте строку, содержащую произвольное количество целых чисел и найдите их сумму.
#
# Sample Input 1:
#
# 1 2
# Sample Output 1:
#
# 3
# Sample Input 2:
#
# 1 2 3
# Sample Output 2:
#
# 6
# Sample Input 3:
#
# 99 234 34 1 0 -5 55 666 42
# Sample Output 3:
#
# 1126

print(sum(list(map(int, input().split()))))
