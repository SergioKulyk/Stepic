# Считайте строку.
#
# Если она содержит число 0, выведите на печать фразу "Division by zero!"
#
# Если она содержит число, отличное от 0,
# то считайте ещё одну строку, содержащую число, и напечатайте результат деления 2-ого числа на 1-е.
# Результат деления округлите до 1 знака после запятой (используйте round).
#
# Sample Input 1:
#
# 0
# Sample Output 1:
#
# Division by zero!
# Sample Input 2:
#
# 3
# 4
# Sample Output 2:
#
# 1.3

a = int(input())
if a:
    print("Division by zero!")
else:
    b = int(input())
    print(round(b / a, 1))
