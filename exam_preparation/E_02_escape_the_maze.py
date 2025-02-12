size = int(input())
matrix = []
traveler_position = []
traveler_health = 100
traveler_defeated = False
exit_reached = False

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == "P":
            traveler_position = [row, col]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()
    matrix[traveler_position[0]][traveler_position[1]] = "-"
    direction = directions[command]
    new_row = traveler_position[0] + direction[0]
    new_col = traveler_position[1] + direction[1]
    if 0 <= new_row < size and 0 <= new_col < size:
        traveler_position = [new_row, new_col]
        if matrix[new_row][new_col] == "M":
            traveler_health -= 40
            if traveler_health > 0:
                matrix[new_row][new_col] = "-"
            else:
                traveler_health = 0
                traveler_defeated = True
                break
        elif matrix[new_row][new_col] == "H":
            traveler_health = min(traveler_health + 15, 100)
            matrix[new_row][new_col] = "-"
        elif matrix[new_row][new_col] == "X":
            exit_reached = True
            break

matrix[traveler_position[0]][traveler_position[1]] = "P"

if traveler_defeated:
    print("Player is dead. Maze over!")
elif exit_reached:
    print("Player escaped the maze. Danger passed!")
print(f"Player's health: {traveler_health} units")
[print(*row, sep="") for row in matrix]
