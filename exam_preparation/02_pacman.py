field_size = int(input())
pacman_position = []
matrix = []
pacman_health = 100
stars_count = 0

for row in range(field_size):
    matrix.append(list(input()))
    for col in range(field_size):
        if matrix[row][col] == "P":
            pacman_position = [int(row), int(col)]
        elif matrix[row][col] == "*":
            stars_count += 1

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix[pacman_position[0]][pacman_position[1]] = "-"
ghost_freezer = 0

while True:
    if stars_count == 0:
        print("Pacman wins! All the stars are collected.")
        break
    if pacman_health <= 0:
        print(f"Game over! Pacman last coordinates [{pacman_position[0]},{pacman_position[1]}]")
        break
    command = input()
    if command == "end":
        break
    direction = directions[command]
    new_row = pacman_position[0] + direction[0]
    new_col = pacman_position[1] + direction[1]
    if not 0 <= new_row < field_size:
        new_row %= field_size
    if not 0 <= new_col < field_size:
        new_col %= field_size
    if matrix[new_row][new_col] == "*":
        stars_count -= 1
    elif matrix[new_row][new_col] == "G":
        if ghost_freezer < 1:
            pacman_health -= 50
        else:
            ghost_freezer = 0
    elif matrix[new_row][new_col] == "F":
        ghost_freezer = 1
    matrix[new_row][new_col] = "-"
    pacman_position = [new_row, new_col]

matrix[pacman_position[0]][pacman_position[1]] = "P"

if pacman_health > 0 and stars_count > 0:
    print("Pacman failed to collect all the stars.")
print(f"Health: {pacman_health}")
if stars_count > 0:
    print(f"Uncollected stars: {stars_count}")
[print(*row, sep="") for row in matrix]
