rows_count = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows_count)]

while True:
    command = input()
    if command == "END":
        break
    action = command.split()[0]
    row_index = int(command.split()[1])
    col_index = int(command.split()[2])
    value = int(command.split()[3])
    if action == "Add":
        if 0 <= row_index <= rows_count - 1 and 0 <= col_index <= len(matrix):
            matrix[row_index][col_index] += int(value)
        else:
            print("Invalid coordinates")
    elif action == "Subtract":
        if 0 <= row_index <= rows_count - 1 and 0 <= col_index <= len(matrix):
            matrix[row_index][col_index] -= int(value)
        else:
            print("Invalid coordinates")

[print(*row, sep=" ") for row in matrix]
