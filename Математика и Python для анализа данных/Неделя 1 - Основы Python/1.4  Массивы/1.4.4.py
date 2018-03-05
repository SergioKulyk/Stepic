# На вход подаётся строка, слова в которой разделены между собой пробелами.
#
# Напечатайте 2, 3 и предпоследнее слова из строки (через пробел)
#
# Sample Input 1:
#
# Some Short String
# Sample Output 1:
#
# Short String Short
# Sample Input 2:
#
# And this is some long line, which consists of a set of words
# Sample Output 2:
#
# this is of

s = input().split()
l = [s[1], s[2], s[-2]]
print(*l)
