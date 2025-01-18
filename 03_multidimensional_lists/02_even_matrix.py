rows = int(input())

matrix = []
for row in range(rows):
    row_data = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(row_data)

print(matrix)
