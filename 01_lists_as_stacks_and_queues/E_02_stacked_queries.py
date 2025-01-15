queries_number = int(input())
numbers_stack = []

for query in range(queries_number):
    command = input().split()
    if len(command) > 1:
        number = int(command[1])
        numbers_stack.append(number)
    elif numbers_stack:
        if command[0] == "2":
            numbers_stack.pop()
        elif command[0] == "3":
            print(max(numbers_stack))
        elif command[0] == "4":
            print(min(numbers_stack))

while numbers_stack:
    if len(numbers_stack) > 1:
        print(numbers_stack.pop(), end=", ")
    else:
        print(numbers_stack.pop())
