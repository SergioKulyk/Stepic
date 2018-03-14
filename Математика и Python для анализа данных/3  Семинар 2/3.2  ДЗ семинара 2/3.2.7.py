# B. front_back

# Рассмотрим разделение строки на две половины.
# Если длина четная, 1я и 2я части имеют одинаковую длину
# Если длина нечетная, мы скажем, что дополнительный символ идет в передней половине
# например, «abcde»: 1я часть - «abc», 2я часть «de».
#
# Напишите функцию front_back(a, b), принимающую 2 строки, a и b, и возвращающую строку формы
# # a-front + b-front + a-back + b-back
#
# Примечание. В этой задаче не нужно ничего считывать и ничего выводить на печать. Только реализовать функцию.
# Sample Input 1:
#
# abcd
# xy
# Sample Output 1:
#
# abxcdy
# Sample Input 2:
#
# abcde
# xyz
# Sample Output 2:
#
# abcxydez
# Sample Input 3:
#
# Kitten
# Donut
# Sample Output 3:
#
# KitDontenut

def front_back(a, b):
    len_a = int(len(a) / 2)
    len_b = int(len(b) / 2)

    if len(a) % 2 != 0:
        len_a += 1

    if len(b) % 2 != 0:
        len_b += 1

    return a[:len_a] + b[:len_b] + a[len_a:] + b[len_b:]

print(front_back("Kitten", "Donut"))
