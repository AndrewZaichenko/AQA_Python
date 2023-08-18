"""
Write generator, which generates numbers in a given range (from a certain number to a certain number)
"""


def generator_of_nums():  # creating of generator function
    for num in range(10, 70, 5):
        yield num


gen = generator_of_nums()  # creating of generator object
print(next(gen))  # getting values one by one using 'next'
print(next(gen))
print(next(gen))
print(next(gen))
print("*************")

for num in gen:  # getting generator values 30-50 using for cycle and certain condition
    if num <= 50:
        print(num)
    else:
        print(f'{num} the last value in cycle')
        break

print("*************")
print(next(gen))  # getting values one by one using 'next'
print(next(gen))
# print(next(gen))  # StopIteration
