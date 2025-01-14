from collections import deque

expression = input().split()
numbers = deque()

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b
}

for element in expression:
    if element not in "+-*/":
        numbers.append(int(element))
    else:
        while len(numbers) > 1:
            first_number = numbers.popleft()
            second_number = numbers.popleft()
            numbers.appendleft(operators[element](first_number, second_number))

print(numbers[0])
