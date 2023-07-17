# Завдання 1: Створіть дві змінні first=10, second=30.
# Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел

first_num = 10
second_num = 30

print(f"The sum of 'first_num' and 'second_num' is equal to {first_num + second_num}")
print(f"The result of subtracting between 'second_num' and 'first_num' is equal to {second_num - first_num}")
print(f"The result of multiplying of 'first_num' and 'second_num' is equal to {first_num * second_num}")
print(f"The result of dividing of 'first_num' by 'second_num' is equal to {first_num / second_num}")
print(f"Raising 'first_num' to the power of 'second_num' is equal to {first_num ** second_num}")
print(f"The modulus of 'second_num' and 'first_num' is equal to {first_num % second_num}")
print(f"The result of floor division of 'second_num' by 'first_num' is equal to {second_num // first_num}")
print('****************************************')

# Завдання 2: Створіть змінну и по черзі запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1.
# Виведіть на екран результат кожного порівняння.

comparison_of_nums = first_num < second_num
print(f"The 'first_num' is less than the 'second_num'--> {comparison_of_nums}")

comparison_of_nums = first_num > second_num
print(f"The 'first_num' is greater than the 'second_num'--> {comparison_of_nums}")

comparison_of_nums = first_num == second_num
print(f"The 'first_num' is equal to the 'second_num'--> {comparison_of_nums}")

comparison_of_nums = first_num != second_num
print(f"The 'first_num' is not equal to the 'second_num'--> {comparison_of_nums}")
print('****************************************')

# Завдання 3: Створіть змінну - резлультат конкатенації строк "Hello " та "world!".

word_hello = "Hello "
word_world = "world!"
concat_words = word_hello + word_world
print(f"The result of words concatenation is '{concat_words}'")
