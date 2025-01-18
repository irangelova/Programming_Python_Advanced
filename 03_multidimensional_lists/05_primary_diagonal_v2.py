matrix_size = int(input())
sum_primary_diagonal = 0

for current_index in range(matrix_size):
    row_data = [int(el) for el in input().split()]
    sum_primary_diagonal += row_data[current_index]

print(sum_primary_diagonal)
