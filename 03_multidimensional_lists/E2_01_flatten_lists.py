entry = input().split("|")
lines = [el.split() for el in entry]
flattened_matrix = []

for row in range(len(lines) - 1, -1, -1):
    for el in lines[row]:
        flattened_matrix.append(el)
print(*flattened_matrix, sep=" ")
