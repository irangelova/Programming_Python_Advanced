rows, columns = [int(el) for el in input().split()]
#matrix = []

matrices_found = 0

# for _ in range(rows):
#     row_data = list(input().split())
#     matrix.append(row_data)

matrix = [input().split() for _ in range(rows)]

for row_index in range(len(matrix) - 1):
    for col_index in range(len(matrix[row_index]) - 1):
        # set_el = set()
        # set_el.add(matrix[row_index][col_index])
        # set_el.add(matrix[row_index][col_index + 1])
        # set_el.add(matrix[row_index + 1][col_index])
        # set_el.add(matrix[row_index + 1][col_index + 1])
        # if len(set_el) == 1:
        #     matrices_found += 1

        if matrix[row_index][col_index] == matrix[row_index][col_index + 1] == matrix[row_index + 1][col_index] == matrix[row_index + 1][col_index + 1]:
            matrices_found += 1

print(matrices_found)
