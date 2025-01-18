import sys

rows, columns = [int(x) for x in input().split(", ")]

matrix = []
max_square = []
max_sum = -sys.maxsize

for _ in range(rows):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)

for row_index in range(len(matrix) - 1):
    for col_index in range(len(matrix[row_index]) - 1):
        current_el = matrix[row_index][col_index]
        el_to_right = matrix[row_index][col_index + 1]
        el_below = matrix[row_index + 1][col_index]
        el_diagonally = matrix[row_index + 1][col_index + 1]
        current_sum = current_el + el_to_right + el_below + el_diagonally
        if current_sum > max_sum:
            max_sum = current_sum
            max_square = [[current_el, el_to_right], [el_below, el_diagonally]]

print(*max_square[0])
print(*max_square[1])
print(max_sum)
