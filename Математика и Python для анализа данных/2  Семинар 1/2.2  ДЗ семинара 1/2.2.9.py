# 9. Числа Фибоначчи

# Напишите функцию fib(n), возвращающую n-е число Фибоначчи.
#
#
# Примечание. Пример вывода дан для n = 1, 2, 5 и 9
#
# В данной задаче не требуется осуществлять вывод - проверка производится для разных чисел!
#
# Sample Input:
#
#
# Sample Output:
#
# 1 1 5 34

def fib(n):
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return n

print(fib(2))