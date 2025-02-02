field_size = int(input())
bunny_position = []
matrix = []

for row in range(field_size):
    matrix.append(input().split())
    for col in range(field_size):
        if matrix[row][col] == "B":
            bunny_position = [row, col]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

max_eggs = float("-inf")
max_direction = ""
max_eggs_positions = []

for direction, move in possible_moves.items():
    eggs = 0
    curr_eggs_matrix = []
    row = bunny_position[0] + move[0]
    col = bunny_position[1] + move[1]

    while 0 <= row < field_size and 0 <= col < field_size:
        if matrix[row][col] == "X":
            break

        eggs += int(matrix[row][col])
        curr_eggs_matrix.append([row, col])
        row += move[0]
        col += move[1]

    if eggs > max_eggs and curr_eggs_matrix:
        max_eggs = eggs
        max_direction = direction
        max_eggs_positions = curr_eggs_matrix

print(max_direction)
print(*[egg_position for egg_position in max_eggs_positions], sep="\n")
print(max_eggs)
