rows, columns = [int(x) for x in input().split(", ")]
sum_elements = 0

matrix = []
for row in range(rows):
    data_row = [int(el) for el in input().split(", ")]
    #sum_elements += sum(data_row)
    matrix.append(data_row)

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        sum_elements += matrix[row_index][col_index]

print(sum_elements)
print(matrix)
