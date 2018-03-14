# A. verbing

# Напишите функцию verbing(s), принимающую на вход строку.
#
# Если длина строки 3 и больше, то добавьте к ней 'ing' в конце
# Если строка уже содержит 'ing', добавьте 'ly'
# Если длина строки меньше 3, верните строку как есть
#
#
# Примечание. В этой задаче не нужно ничего считывать и ничего выводить на печать. Только реализовать функцию.
# Sample Input 1:
#
# hail
# Sample Output 1:
#
# hailing
# Sample Input 2:
#
# swiming
# Sample Output 2:
#
# swimingly
# Sample Input 3:
#
# do
# Sample Output 3:
#
# do

def verbing(s):
    if len(s) >= 3:
        if s[-3:] == "ing":
            return s + "ly"
        else:
            return s + "ing"
    else:
        return s

# print(verbing("hail"))
# print(verbing("swiming"))
# print(verbing("do"))
