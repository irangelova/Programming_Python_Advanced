rows, columns = [int(x) for x in input().split(", ")]

matrix = []
for _ in range(rows):
    row_data = [int(el) for el in input().split()]
    matrix.append(row_data)

for col_index in range(columns):
    current_col_sum = 0
    for row_index in range(rows):
        current_col_sum += int(matrix[row_index][col_index])
    print(current_col_sum)
