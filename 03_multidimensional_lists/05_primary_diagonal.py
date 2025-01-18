matrix_size = int(input())
sum_primary_diagonal = 0

matrix = []

for _ in range(matrix_size):
    row_data = [int(el) for el in input().split()]
    matrix.append(row_data)

for row_index in range(len(matrix)):
    sum_primary_diagonal += matrix[row_index][row_index]

print(sum_primary_diagonal)
