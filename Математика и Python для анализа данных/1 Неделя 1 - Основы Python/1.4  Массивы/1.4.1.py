# На вход подаётся строка из 3 натуральных чисел.
#
# Найдите сумму чисел.
#
# Sample Input:
#
# 5 0 3
# Sample Output:
#
# 8

numbers = map(int, input().split())
print(sum(numbers))
