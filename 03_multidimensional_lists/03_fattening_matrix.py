rows = int(input())

matrix = []
for row_index in range(rows):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)

flattened_matrix = []
for row in range(len(matrix)):
    for el in matrix[row]:
        flattened_matrix.append(el)

print(flattened_matrix)