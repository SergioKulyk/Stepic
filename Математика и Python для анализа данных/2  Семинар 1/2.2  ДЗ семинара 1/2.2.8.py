# 8. front_x (с пустыми строками)

# Напишите функцию front_x(words), которая на вход принимает список строк и сортирует его по правилам:
#
# слова, начинающиеся с символа "x", идут первыми
# в лексикографическом порядке.
# Важно! Список может содержать пустые строки - "" - их нельзя выкидывать и при их обработке функция не должна "падать".
#
#
#
#
#
# Примечание. Пример вывода дан для words = ['mix', 'extra', '', 'x-files', 'xyz', 'xapple', 'apple']
#
# В данной задаче не требуется осуществлять вывод - проверка производится для разных списков!
#
# Sample Input:
#
#
# Sample Output:
#
# ['x-files', 'xapple', 'xyz', '', 'apple', 'extra', 'mix']

def front_x(words):
    x_first = [word for word in words if len(word) != 0 and word[0] == 'x']
    not_x_first = [word for word in words if len(word) == 0 or word[0] != 'x']
    return sorted(x_first) + sorted(not_x_first)


print(front_x(['mix', 'extra', '', 'x-files', 'xyz', 'xapple', 'apple']))