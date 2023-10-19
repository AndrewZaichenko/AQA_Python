"""
Create a generator with the following parameters:
start - first prime integer to yield
end - last prime integer to yield
Ex. def prime_numbers(start, end):

The generator should yield all prime numbers from the range(start, end) in the next code:

print(f"Found next prime numbers from the range /{{start}:{end}/}")

for num in prime_numbers(start, end):
  print(num, end=", ")

Fix errors from the code above.
To solve this task you can use the next article -
https://www.enjoymathematics.com/blog/how-to-find-prime-numbers-in-a-range
Upload the task to the homework directory on GitHub
"""

import math


def prime_numbers(start_num, end_num):

    count = 2
    while True:
        isprime = True

        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break

        if isprime and start_num <= count <= end_num:
            yield count

        count += 1


start_num = int(input("Please enter the start number of the range-> "))
end_num = int(input("Please enter the end number of the range -> "))

print(f"Found next prime numbers from the range {start_num}:{end_num}")

for i in prime_numbers(start_num, end_num):
    print(i, end=", ")
