# Считайте натуральное число n
# Найдите самый маленький натуральный делитель числа x, отличный от 1 (2 <= x <= 30000).
# Sample Input:
#
# 2589
# Sample Output:
#
# 3

n = int(input())
for i in range(2, 30001):
    if n % i == 0:
        print(i)
        break
