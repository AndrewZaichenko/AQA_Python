"""
Порахувати кількість унікальних символів в строці.
Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()
"""

user_string = input("Please enter a sentence to discover the quantity of unique symbols -> ").replace(" ", "").lower()
# print(user_string)
user_set = set(user_string)
print(f"The unique symbols are {user_set}")

if len(user_set) > 10:
    print(f"That's {True}, {len(user_set)} is greater than 10.")
else:
    print(f"{False}, {len(user_set)} is less than 10.")
