# kaprekar_check(n)

# В прошлый раз когда мы запустили Процесс Капрекара (для 4х значных чисел), то нам пришлось добавить проверку:
# число не должно иметь всех одинаковых цифр
# быть больше 1000
# Так же мы не учитывали ограничение, заданное условием задачи:
# на вход подавались только 4х значные числа
#
# Напишите функцию kaprekar_check(n), принимающую на вход 1 натуральное число,
# а возвращающую логическое значение (True или False)
# в зависимости от предварительной проверки на возможность прохождения Процесса Капрекара для него.
#
# Критерии возможности:
# число 3, 4 или 6 значное
# не все цифры в числе одинаковые
# число не равно 100, 100 или 100 000
#
# Примечание. В этой задаче не нужно ничего считывать и ничего выводить на печать. Только реализовать функцию.
#
# Рекомендация. Имеет смысл использовать функцию numerics(n) совместно с множествами (set())
# в процессе определения числа цифр в числе.
# Sample Input 1:
#
# 4086
# Sample Output 1:
#
# True
# Sample Input 2:
#
# 486
# Sample Output 2:
#
# True
# Sample Input 3:
#
# 408886
# Sample Output 3:
#
# True
# Sample Input 4:
#
# 86
# Sample Output 4:
#
# False
# Sample Input 5:
#
# 1234567
# Sample Output 5:
#
# False
# Sample Input 6:
#
# 100
# Sample Output 6:
#
# False
# Sample Input 7:
#
# 1000
# Sample Output 7:
#
# False
# Sample Input 8:
#
# 1111
# Sample Output 8:
#
# False

# Recomendation to use numerics(n) and set() for counting

def numerics(n):
    return list(map(int, str(n)))


def kaprekar_check(n):
    if n == 100 or n == 1_000 or n == 100_000:
        return False
    elif len(set(numerics(n))) == 1:
        return False

    length = len(numerics(n))
    return length == 3 or length == 4 or length == 6
