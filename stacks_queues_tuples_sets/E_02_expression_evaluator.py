from math import floor
from collections import deque

expression = input()
numbers = deque()
result = 0

for element in expression:
    if element.isdigit():
        numbers.append(element)
    else:
        first_number = numbers.popleft()
        second_number = numbers.popleft()
        if element == "+":
            result = first_number + second_number
        elif element == "-":
            result = first_number - second_number
        elif element == "*":
            result = first_number * second_number
        elif element == "/":
            result = floor(first_number / second_number)
        numbers.append(result)
        numbers.rotate(1)

print()
