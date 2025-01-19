rows, columns = [int(el) for el in input().split()]
max_sum = -float("inf")
max_row = max_column = 0

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

for row_index in range(len(matrix) - 2):
    for col_index in range(columns - 2):
        current_sum = 0
        for r in range(row_index, row_index + 3):
            for c in range(col_index, col_index + 3):
                current_sum += matrix[r][c]
        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row_index
            max_column = col_index

print(f"Sum = {max_sum}")
max_submatrix = [matrix[r][max_column:max_column + 3] for r in range(max_row, max_row + 3)]
[print(*row) for row in max_submatrix]
