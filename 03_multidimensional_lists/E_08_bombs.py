matrix_size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(matrix_size)]

bombs = input().split()
bombs_positions = [bomb.split(",") for bomb in bombs]
active_cells = 0
sum_active_cells = 0

for bomb in bombs_positions:
    bomb_row = int(bomb[0])
    bomb_col = int(bomb[1])
    current_value = matrix[bomb_row][bomb_col]
    start_row = 0 if bomb_row == 0 else -1
    end_row = 1 if bomb_row == (matrix_size - 1) else 2
    start_col = 0 if bomb_col == 0 else -1
    end_col = 1 if bomb_col == (matrix_size - 1) else 2
    for cell_row in range(start_row, end_row):
        for cell_col in range(start_col, end_col):
            if matrix[bomb_row + cell_row][bomb_col + cell_col] > 0:
                matrix[bomb_row + cell_row][bomb_col + cell_col] -= current_value

for row_index in range(matrix_size):
    for col_index in range(matrix_size):
        if matrix[row_index][col_index] > 0:
            active_cells += 1
            sum_active_cells += matrix[row_index][col_index]

print(f"Alive cells: {active_cells}")
print(f"Sum: {sum_active_cells}")
[print(*row, sep=" ") for row in matrix]
