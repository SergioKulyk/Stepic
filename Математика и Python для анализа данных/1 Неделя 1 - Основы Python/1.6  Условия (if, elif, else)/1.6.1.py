# Римские цифры
# Считайте число (см таблицу) в арабской записи и выведите на печать, соответствующую ему римскую цифру:
#
# 1 - I
# 5 - V
# 10 - X
# 50 - L
# 100 - C
# 500 - D
# 1000 - M
#
# Sample Input 1:
#
# 1
# Sample Output 1:
#
# I
# Sample Input 2:
#
# 5
# Sample Output 2:
#
# V

d = int(input())

if d == 1:
    print('I')
if d == 5:
    print('V')
elif d == 10:
    print('X')
elif d == 50:
    print('L')
elif d == 100:
    print('C')
elif d == 500:
    print('D')
elif d == 1000:
    print('M')
