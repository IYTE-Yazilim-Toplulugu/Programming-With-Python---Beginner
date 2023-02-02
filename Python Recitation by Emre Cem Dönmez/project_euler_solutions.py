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

"""
import math
counter = 1

for i in range(2, 21):
    counter *= i // math.gcd(i, counter)

print(counter)
"""

# Sum square difference

"""
counter0 = sum(number ** 2 for number in range(1, 101))
counter1 = (100 * 101 / 2) ** 2

print(counter1 - counter0)
"""

# 10001st prime
"""
def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for divisior in range(3, int(number ** 0.5) + 1, 2):
        if number % divisior == 0:
            return False

    return True


primes = []

number = 2
while len(primes) < 10001:
    if is_prime(number):
        primes.append(number)

    number += 1

print(primes[-1])
"""

# Largest product in a series
"""
number = str(73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450)

number = "".join(number.split("\n"))
maximum = float("-inf")

for start_index in range(1000 - 12):
    segment = number[start_index: start_index + 13]
    counter = 1

    for char in segment:
        counter *= int(char)

    maximum = max(maximum, counter)
    #if counter > maximum:
    #    maximum = counter

print(maximum)
"""

# Special Pythagorean triplet
"""
for a in range(1, 1001):
    for b in range(a + 1, 1001):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
            print(a * b * c)
            exit()
"""

# Summation of primes
"""
def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for divisior in range(3, int(number ** 0.5) + 1, 2):
        if number % divisior == 0:
            return False

    return True


counter = 0

for number in range(1, 2000000):
    if is_prime(number):
        counter += number

print(counter)
"""
