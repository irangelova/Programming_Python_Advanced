rows = int(input())
matrix = []

for _ in range(rows):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)

primary_diagonal = []
secondary_diagonal = []
sum_primary_diagonal = 0
sum_secondary_diagonal = 0

for row_index in range(len(matrix)):
    sum_primary_diagonal += matrix[row_index][row_index]
    primary_diagonal.append((matrix[row_index][row_index]))

#primary_diagonal = [matrix[row_index][row_index] for row_index in range(len(matrix))]

for row_index in range(len(matrix)):
    sum_secondary_diagonal += matrix[row_index][rows - row_index - 1]
    secondary_diagonal.append(matrix[row_index][rows - row_index - 1])

#primary_diagonal = [matrix[row_index][rows - row_index - 1] for row_index in range(len(matrix))]

print(f"Primary diagonal: {', '.join(str(el) for el in primary_diagonal)}. Sum: {sum_primary_diagonal}")
print(f"Secondary diagonal: {', '.join(str(el) for el in secondary_diagonal)}. Sum: {sum_secondary_diagonal}")
