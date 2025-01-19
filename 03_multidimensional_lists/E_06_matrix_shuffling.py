def is_valid_position(r1, c1, r2, c2, matrix_rows, matrix_columns):
    return 0 <= r1 < matrix_rows and 0 <= r2 < matrix_rows and 0 <= c1 < matrix_columns and 0 <= c2 < matrix_columns


rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]


while True:
    entry = input()
    if entry == "END":
        break
    command = entry.split()
    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue
    row1, col1, row2, col2 = [int(x) for x in command[1:]]
    if is_valid_position(row1, col1, row2, col2, rows, columns):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")
