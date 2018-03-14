# kaprekar_loop(n)

# Напишите функцию kaprekar_loop(n), которая принимает целое 4х значное число
# (больше 1000, содержащее хотя бы 2 разные цифры), и запускающую "Процесс Капрекара",
# выводящее на печать каждое число цикла с новой строки до тех пор, пока не будет получено число 6174.
#
# Для написания вашей функции используйте написанные на предыдущих шагах функции numerics(n) и
# kaprekar_step(L).
#
# Примечание. В этой задаче не нужно ничего считывать и ничего выводить на печать. Только реализовать функцию.
# Sample Input 1:
#
# 6174
# Sample Output 1:
#
# 6174
# Sample Input 2:
#
# 8654
# Sample Output 2:
#
# 8654
# 4086
# 8172
# 7443
# 3996
# 6264
# 4176
# 6174

def numerics(n):
    return list(map(int, list(str(n))))

def kaprekar_step(L):
    a = ''.join(map(str, sorted(L)))
    b = int(a[::-1])
    a = int(a)
    return b - a

def kaprekar_loop(n):
    while n != 6174:
        print(n)
        n = kaprekar_step(numerics(n))
    print(n)
