field_size = int(input())
matrix = []
player_position = []
collected_stars = 2

for row in range(field_size):
    matrix.append(input().split())
    for col in range(field_size):
        if matrix[row][col] == "P":
            player_position = [row, col]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while 1 <= collected_stars < 10:
    command = input()
    direction = directions[command]
    new_row = player_position[0] + direction[0]
    new_col = player_position[1] + direction[1]
    if 0 <= new_row < field_size and 0 <= new_col < field_size:
        if matrix[new_row][new_col] == "*":
            matrix[player_position[0]][player_position[1]] = "."
            collected_stars += 1
            matrix[new_row][new_col] = "P"
            player_position = [new_row, new_col]
        elif matrix[new_row][new_col] == "#":
            collected_stars -= 1
        else:
            matrix[player_position[0]][player_position[1]] = "."
            matrix[new_row][new_col] = "P"
            player_position = [new_row, new_col]
    else:
        if matrix[0][0] == "*":
            collected_stars += 1
        matrix[player_position[0]][player_position[1]] = "."
        player_position = [0, 0]
        matrix[player_position[0]][player_position[1]] = "P"

if collected_stars >= 10:
    print("You won! You have collected 10 stars.")
else:
    print("Game over! You are out of any stars.")
print(f"Your final position is [{player_position[0]}, {player_position[1]}]")
[print(*row, sep=" ") for row in matrix]

