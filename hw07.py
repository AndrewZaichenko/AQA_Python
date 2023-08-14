"""
Create a file with numbers (in a few rows)
Read this file, and print the sum of all numbers (create a new function for it)
Use try\except block to avoid other symbols except numbers in the file
"""

with open("file_with_nums.txt", "x") as file:
    i = 0
    while i < 5:
        file.write(input("Please enter a number -> ") + '\n')
        i += 1


def sum_of_nums_from_file():
    sum_of_nums = 0
    with open("file_with_nums.txt") as file_to_read:
        for elem in file_to_read.readlines():
            try:
                sum_of_nums = sum_of_nums + int(elem.strip())
            except:
                print(f'{elem.strip()} is not a number')
            finally:
                print(f'For current iteration sum is equal to {sum_of_nums}')
    return sum_of_nums


print(f'The sum of nums in file equals to {sum_of_nums_from_file()}')
