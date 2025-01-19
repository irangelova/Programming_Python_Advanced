import sys

rows, columns = [int(el) for el in input().split()]
max_sum = -sys.maxsize
#max_sum = -float("inf")
max_square = []

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

for row_index in range(len(matrix) - 2):
    for col_index in range(columns - 2):
        current_el = matrix[row_index][col_index]
        el_to_right = matrix[row_index][col_index + 1]
        el2_to_right = matrix[row_index][col_index + 2]
        el_below = matrix[row_index + 1][col_index]
        el_diagonally = matrix[row_index + 1][col_index + 1]
        el_2right_bellow = matrix[row_index + 1][col_index + 2]
        el_2below = matrix[row_index + 2][col_index]
        el_2below_right = matrix[row_index + 2][col_index + 1]
        el2_diagonally = matrix[row_index + 2][col_index + 2]
        current_sum = current_el + el_to_right + el2_to_right + el_below + el_diagonally + el_2right_bellow + el_2below + el_2below_right + el2_diagonally
        if current_sum > max_sum:
            max_sum = current_sum
            max_square = [[current_el, el_to_right, el2_to_right],
                          [el_below, el_diagonally, el_2right_bellow],
                          [el_2below, el_2below_right, el2_diagonally]]

print(f"Sum = {max_sum}")
print(*max_square[0])
print(*max_square[1])
print(*max_square[2])
