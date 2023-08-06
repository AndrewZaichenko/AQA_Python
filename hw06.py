"""
Написати функцію, яка буде рекурсивно вираховувати число фібоначчі.

Число фібоначчі - це число, яке дорівнює суммі двох попередніх в послідовності (це і повинно бути в рекурсії). Закінчується на двох одиницях

1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1587
"""


def fibo_func_limit(lim_num, first_num=1, second_num=1):
    fibo_num = first_num + second_num
    if fibo_num >= lim_num:
        return print(
            f"You have reached the limit - the fibonacci number is {fibo_num}, and it's greater than {lim_num}")
    else:
        print(f"Fibonacci number for current iteration --> {fibo_num}")
        return fibo_func_limit(lim_num, second_num, fibo_num)


fibo_func_limit(int(input("Enter a limit that fibonacci number should not exceed --> ")))


def fibo_func(first_num=1, second_num=1):
    fibo_num = first_num + second_num
    if str(fibo_num).endswith("11", -2):
        return print(f"You have reached the value that ends with '11' - the fibonacci number is --> {fibo_num}")
    else:
        print(f"Fibonacci number for current iteration --> {fibo_num}")
        return fibo_func(second_num, fibo_num)


fibo_func()
