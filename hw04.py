"""
1. Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є буква "о" (враховуються як великі так і маленькі).
Цикл не повинен завершитися, якщо користувач ввів слово без букви "о".
"""
user_word = input("Please enter a word with letter 'O' --> ")

while "o" not in user_word and "O" not in user_word:  # or it's possible to use user_word.lowercase()
    user_word = input("The letter 'O' is absent in your word, please enter another one --> ")

print(f"Yes, the letter 'О' is present in word '{user_word}'")


"""
2. Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. 
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. 
Данні в лісті можуть бути будь якими
"""

init_lst = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst_str = []
lst_int = []
lst_bool = []

for elem in init_lst:
    if type(elem) == str:
        lst_str.append(elem)
    elif type(elem) == int:
        lst_int.append(elem)
    else:
        lst_bool.append(elem)

print(f"The list of elements with type 'string' -> {lst_str}")
print(f"The list of elements with type 'int' -> {lst_int}")
print(f"The list of elements with type 'boolean' -> {lst_bool}")


"""
3. Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
"""

list_of_nums = [45, 0, 3, 56, 3, 73, 83, 32, 678, 35, 24, 7, 23, 1, 56, 78, 99, 100, 12, 2, 4]
sum_of_even = 0

for num_in_lst in list_of_nums:
    if num_in_lst % 2 == 0:
        sum_of_even = sum_of_even + num_in_lst

print(f'The sum of even nums in list equals {sum_of_even}')
