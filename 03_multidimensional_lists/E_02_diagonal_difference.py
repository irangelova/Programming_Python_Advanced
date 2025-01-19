rows = int(input())
#matrix = []

# for _ in range(rows):
#     row_data = list(input().split())
#     matrix.append(row_data)

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

sum_primary_diagonal = 0
sum_secondary_diagonal = 0

for row_index in range(len(matrix)):
    sum_primary_diagonal += int(matrix[row_index][row_index])
    sum_secondary_diagonal += int(matrix[row_index][rows - row_index - 1])

print(abs(sum_primary_diagonal - sum_secondary_diagonal))
