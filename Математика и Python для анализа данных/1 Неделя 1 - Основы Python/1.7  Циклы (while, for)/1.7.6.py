# Считайте целое число n
# Напечатайте кубы всех натуральных чисел, меньших |n|, каждое с новой строки.
# Sample Input 1:
#
# 4
# Sample Output 1:
#
# 1
# 8
# 27
# Sample Input 2:
#
# -5
# Sample Output 2:
#
# 1
# 8
# 27
# 64

n = int(input())
for i in range(1, abs(n)):
    print(i**3)
