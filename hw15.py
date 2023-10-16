"""
Create a generator with the following parameters:

start - first prime integer to yield
end - last prime integer to yield
Ex. def prime_numbers(start, end):

The generator should yield all prime numbers from the range(start, end) in the next code:

Fix errors from the code above.

To solve this task you can use the next article - https://www.enjoymathematics.com/blog/how-to-find-prime-numbers-in-a-range

Upload the task to the homework directory on GitHub
"""

# import math
from math import pow, ceil

# def prime_numbers(start_num, end_num):
#
#     count = start_num
#     while True:
#         isprime = True
#
#         for x in range(2, int(math.sqrt(count) + 1)):
#             if count % x == 0:
#                 isprime = False
#                 break
#
#         if isprime and count >= start_num and count <= end_num:
#             yield count
#
#         count += 1
#
#
# start_num = int(input("Please enter the range start number -> "))
# end_num = int(input("Please enter the range end number -> "))
#
# print(f"Found next prime numbers from the range {start_num}:{end_num}")
#
# for i in prime_numbers(start_num, end_num):
#     print(i, end=", ")


def sieve_of_eratosthenes(n):
    sieve = [True for i in range(n+1)]
    sieve[1] = False
    primes = []

    for i in range(2, ceil(pow(n, 0.5)) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve = False

    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)

    return primes

print(sieve_of_eratosthenes(100))

