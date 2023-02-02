# Python If-Else
"""
n = int(input())
message = ""

if n % 2 == 1:
    message = "Weird"
elif n % 2 == 0 and 2 <= n <= 5:
    message = "Not Weird"
elif n % 2 == 0 and 6 <= n <= 20:
    message = "Weird"
else:
    message = "Not Weird"

print(message)
"""

# Arithmetic Operators
"""
a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)
"""

# Print Function
"""
n = int(input())

for i in range(1, n + 1):
    print(i, end="")
"""

# Find the Runner-Up Score!

n = int(input())
numbers = input().split(" ")
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

numbers = list(set(numbers))
numbers.sort()

print(numbers[-2])
