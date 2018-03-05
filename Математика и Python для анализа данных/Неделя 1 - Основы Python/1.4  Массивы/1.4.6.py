# На вход подаётся 1 строка, слова в которой разделены пробелами.
#
# Напечатайте через пробел число слов в строке и число слов "one" в строке.
#
#
#
# Примечание1. Учитывайте вхождение только слова полностью в нижнем регистре - "one". "One", "ONE" и т.п. не учитывайте.
#
# Примечание2. Число элементов списка L можно получить с помощью конструкции len(L)
#
# Sample Input 1:
#
# One string short and one long
# Sample Output 1:
#
# 6 1
# Sample Input 2:
#
# one cat and one dog are friends
# Sample Output 2:
#
# 7 2

L = input().split()
print(len(L), L.count("one"))
