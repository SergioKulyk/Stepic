# C1. mimic_dict

# Напишите функцию mimic_dict(string), которая принимает на вход строковую переменную
# (может содержать пробелы, табуляцию, переносы строк), возвращающую «имитирующий» словарь,
# который соотносит каждое появившееся слово, со списком всех слов, которые следуют за этим словом.
#
# Для "входа" в словарь используйте в качестве ключа пустую строку, в соответствие которой будет поставлено 1 слово.
#
# Примечание. В этой задаче не нужно ничего считывать и ничего выводить на печать. Только реализовать функцию.
#
# Sample Input 1:
#
# Uno dos tres cuatro cinco
# Sample Output 1:
#
# {"": ["Uno"], "Uno": ["dos"], "dos": ["tres"], "tres": ["cuatro"], "cuatro": ["cinco"]}
# Sample Input 2:
#
# a cat and a dog
# a fly
# Sample Output 2:
#
# {"": ["a"], "a": ["cat", "dog", "fly"], "cat": ["and"], "and": ["a"], "dog": ["a"]}

def mimic_dict(string):
    m = {}
    if len(string) <= 0:
        return m

    m[""] = string.split()[0]
    words = string.split()
    i = 0

    while i < len(words) - 1:
        if words[i] in m:
            m[words[i]] = m[words[i]] + words[i]
        else:
            m[words[i]] = list([words[i + 1]])
        i += 1
    return m

# print(mimic_dict("Uno dos tres cuatro cinco"))
# print(mimic_dict("a cat and a dog\na fly"))
