# Шаг 2.1 - проход по списку
# На вход подаётся 1 строка.
#
# Напечатайте в 1 строку все 1-е символы из каждого слова через пробел.
#
# Для разделения строки на слова можно использоваться функцию split():
#
# S = 'Some string'
# L = S.split() # ['Some', 'string']
#
# Sample Input:
#
# Hello my friends
# Sample Output:
#
# H m f

import re

S = input()
for word in re.split('[^A-z]', S):
    if word:
        print(word[0], end=' ')
