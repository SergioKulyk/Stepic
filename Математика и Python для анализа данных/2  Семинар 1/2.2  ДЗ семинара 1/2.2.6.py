# 6. Сумма чисел
# Считайте строку (используйте input()), содержащую 1 натуральное число n
#
# Найдите сумму всех чисел от 0 до n, которые делятся на 5, но не делятся на 3
# Sample Input 1:
#
# 100
# Sample Output 1:
#
# 735
# Sample Input 2:
#
# 422
# Sample Output 2:
#
# 11760

n = int(input())  # Input and convert to int
print([i for i in range(n) if (i % 5 == 0) and (i % 3 != 0)])
res = sum([i for i in range(0, n + 1, 5) if (i % 5 == 0) and (i % 3 != 0)])
print(res)
