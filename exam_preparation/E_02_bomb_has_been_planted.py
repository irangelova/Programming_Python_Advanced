rows, columns = [int(el) for el in input().split(", ")]
matrix = []
ct_position = []
bomb_position = []
TIME_LEFT = 16
bomb_exploded = False
ct_killed = False
bomb_defused = False
not_enough_time = False


for row in range(rows):
    matrix.append(list(input()))
    for col in range(columns):
        if matrix[row][col] == "C":
            ct_position = [row, col]
        elif matrix[row][col] == "B":
            bomb_position = [row, col]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

current_ct_position = [ct_position[0], ct_position[1]]
needed_seconds = 0

while True:
    command = input()
    if command != "defuse":
        current_direction = directions[command]
        if TIME_LEFT >= 1:
            new_row = current_ct_position[0] + current_direction[0]
            new_col = current_ct_position[1] + current_direction[1]
            TIME_LEFT -= 1
            if 0 <= new_row < rows and 0 <= new_col < columns:
                current_ct_position = [new_row, new_col]
            else:
                continue
            if matrix[new_row][new_col] == "T":
                matrix[new_row][new_col] = "*"
                ct_killed = True
                break
        else:
            bomb_exploded = True
            break
    else:
        if current_ct_position != bomb_position:
            TIME_LEFT -= 2
        else:
            if TIME_LEFT >= 4:
                TIME_LEFT -= 4
                matrix[bomb_position[0]][bomb_position[1]] = "D"
                bomb_defused = True
            else:
                matrix[bomb_position[0]][bomb_position[1]] = "X"
                needed_seconds = abs(TIME_LEFT - 4)
                not_enough_time = True
            break
    if TIME_LEFT <= 0:
        not_enough_time = True
        break

if bomb_exploded or not_enough_time:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {needed_seconds} second/s.")
if bomb_defused:
    print("Counter-terrorist wins!")
    print(f"Bomb has been defused: {TIME_LEFT} second/s remaining.")
if ct_killed:
    print("Terrorists win!")

[print(*row, sep="") for row in matrix]
