"""
1. Напишіть функцію, яка приймає два аргументи.
 - Якщо обидва аргумени відносяться до числових типів функція пермножує ці аргументи і повертає результат
 - Якшо обидва аргументи відносяться до типу стрінг функція обʼєднує їх в один і повертає
 - В будь-якому іншому випадку - функція повертає кортеж з двох агрументів
 - Імпортуйте цю функцію, і викличте в іншому файлі
"""


def operations_with_two_args(first_arg, second_arg):
    if type(first_arg) == int and type(second_arg) == int:
        multiplying = first_arg * second_arg
        return print(f"Both arguments are integer, the result of multiplying is {multiplying}")
    elif type(first_arg) == str and type(second_arg) == str:
        concatenation = first_arg + second_arg
        return print(f"Both arguments are string, the result of concatenation is {concatenation}")
    else:
        return print(f"Just a tuple {first_arg, second_arg}")
