# Multiples of 3 or 5
"""
counter = 0

for number in range(1, 1000):
    if number % 3 == 0 or number % 5 == 0:
        counter += number

print(counter)
"""

# Even Fibonacci numbers

"""
fibonacci_numbers = [1, 2]

while fibonacci_numbers[-1] + fibonacci_numbers[-2] < 4000000:
    fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])

counter = 0

for fibonacci_number in fibonacci_numbers:
    if fibonacci_number % 2 == 0:
        counter += fibonacci_number

print(counter)
"""
"""
counter = 0
a = 1
b = 2

while b < 4000000:
    if b % 2 == 0:
        counter += b

    temp = a
    a = b
    b = temp + b

print(counter)
"""

# Largest prime factor
"""
n = 600851475143
lpf = 0

divisior = 2
while divisior <= n:
    if n % divisior == 0:
        lpf = divisior

        while n % divisior == 0:
            n //= divisior

    divisior += 1

# too slow
for divisior in range(2, n + 1):
    if n % divisior == 0:
        lpf = divisior

        while n % divisior == 0:
            n //= divisior


print(lpf)
"""

# Largest palindrome product
"""
max_palindrome = 0

for number0 in range(100, 1000):
    for number1 in range(100, 1000):
        product = str(number0 * number1)
        if product == product[::-1]:
            max_palindrome = max(max_palindrome, int(product))

print(max_palindrome)
"""

# Smallest multiple

"""
# too slow
number = 10

while True:
    is_number_divisible = True

    for divisior in range(2, 21):
        if number % divisior != 0:
            is_number_divisible = False
            break

    if is_number_divisible:
        break

    number += 1

print(number)
"""

# a * b = lcm(a, b) * gcd(a, b)
# a * b / gcd(a, b) = lcm(a, b)

# lcm(1, 2, ... , 20) = lcm(lcm(...lcm(lcm(1, 2), 3)))
# Euclidean algorithm

import math
counter = 1

for i in range(2, 21):
    counter *= i // math.gcd(i, counter)

print(counter)
