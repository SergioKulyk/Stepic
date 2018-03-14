# Считывайте целые числа из потока ввода по одному до тех пор, пока не встретите строку "The End".
#
# Выведите на печать сумму считанных чисел.
#
# Sample Input 1:
#
# 3
# 5
# The End
# Sample Output 1:
#
# 8
# Sample Input 2:
#
# 5
# 42
# 6
# -4
# The End
# 9999
# Sample Output 2:
#
# 49

s = 0
inp = input()
while inp != "The End":
    s += int(inp)
    inp = input()
print(s)
