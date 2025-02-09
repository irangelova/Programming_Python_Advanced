field_size = int(input())
matrix = []
bee_position = []
energy = 15
collected_nectar = 0
hive_reached = False
nectar_not_collected = False

for row in range(field_size):
    matrix.append(list(input()))
    for col in range(field_size):
        if matrix[row][col] == "B":
            bee_position = [row, col]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix[bee_position[0]][bee_position[1]] = "-"
energy_restoration = 0

while True:
    command = input()
    direction = directions[command]
    new_row = int(bee_position[0] + direction[0])
    new_col = int(bee_position[1] + direction[1])
    energy -= 1
    if not 0 <= new_row < field_size:
        new_row %= field_size
    if not 0 <= new_col < field_size:
        new_col %= field_size
    bee_position = [new_row, new_col]
    if (matrix[new_row][new_col]).isdigit():
        collected_nectar += int(matrix[new_row][new_col])
        matrix[new_row][new_col] = "-"
    elif matrix[new_row][new_col] == "H":
        matrix[new_row][new_col] = "-"
        hive_reached = True
        break
    if energy <= 0:
        if collected_nectar < 30:
            nectar_not_collected = True
            break
        else:
            if energy_restoration == 0:
                energy_restoration += 1
                energy += (collected_nectar - 30)
                collected_nectar = 30
            else:
                nectar_not_collected = True
                break
            if energy == 0:
                nectar_not_collected = True
                break

matrix[bee_position[0]][bee_position[1]] = "B"

if hive_reached:
    if collected_nectar >= 30:
        print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
    else:
        print("Beesy did not manage to collect enough nectar.")
elif nectar_not_collected:
    print("This is the end! Beesy ran out of energy.")
[print(*row, sep="") for row in matrix]
