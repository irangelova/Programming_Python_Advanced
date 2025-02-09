grid_size = int(input())
resources = 100
matrix = []
spaceship_position = []
spaceship_lost = False
planet_b_reached = False
resources_used = False

for row in range(grid_size):
    matrix.append(input().split())
    for col in range(grid_size):
        if matrix[row][col] == "S":
            spaceship_position = [row, col]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix[spaceship_position[0]][spaceship_position[1]] = "."

while True:
    command = input()
    direction = directions[command]
    new_row = spaceship_position[0] + direction[0]
    new_col = spaceship_position[1] + direction[1]
    if not 0 <= new_row < grid_size or not 0 <= new_col < grid_size:
        spaceship_lost = True
        break
    resources -= 5
    if matrix[new_row][new_col] == "R":
        resources = resources + 10 if resources <= 90 else 100
    elif matrix[new_row][new_col] == "M":
        resources -= 5
        matrix[new_row][new_col] = "."
    spaceship_position = [new_row, new_col]
    if matrix[new_row][new_col] == "P":
        planet_b_reached = True
        break

    if resources < 5:
        resources_used = True
        break

if matrix[spaceship_position[0]][spaceship_position[1]] != "P":
    matrix[spaceship_position[0]][spaceship_position[1]] = "S"

if planet_b_reached:
    print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
elif resources_used:
    print("Mission failed! The spaceship was stranded in space.")
elif spaceship_lost:
    print(f"Mission failed! The spaceship was lost in space.")
[print(*row) for row in matrix]
