SIZE = 5
matrix = []
my_position = []
targets = []
targets_hit = 0
list_hit_targets = []

for row in range(SIZE):
    matrix.append(input().split())
    for col in range(SIZE):
        if matrix[row][col] == "A":
            my_position = [row, col]
        elif matrix[row][col] == "x":
            targets.append((row, col))

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

count_commands = int(input())

for _ in range(count_commands):
    command = input()
    action = command.split()[0]
    direction = command.split()[1]

    if action == "move":
        steps = int(command.split()[2])
        move = possible_moves[direction]
        new_position_row = my_position[0] + (move[0] * steps)
        new_position_col = my_position[1] + (move[1] * steps)
        if 0 <= new_position_row < SIZE and 0 <= new_position_col < SIZE and matrix[new_position_row][new_position_col] == ".":
            matrix[my_position[0]][my_position[1]] = "."
            matrix[new_position_row][new_position_col] = "A"
            my_position = [new_position_row, new_position_col]
    elif action == "shoot":
        move = possible_moves[direction]
        new_position_row = my_position[0] + move[0]
        new_position_col = my_position[1] + move[1]
        while 0 <= new_position_row < SIZE and 0 <= new_position_col < SIZE:
            if matrix[new_position_row][new_position_col] == "x":
                matrix[new_position_row][new_position_col] = "."
                list_hit_targets.append([new_position_row, new_position_col])
                targets_hit += 1
                break
            new_position_row += move[0]
            new_position_col += move[1]

        if len(targets) == targets_hit:
            break

if len(targets) == targets_hit:
    print(f"Training completed! All {targets_hit} targets hit.")
else:
    print(f"Training not completed! {len(targets) - targets_hit} targets left.")
print(*list_hit_targets, sep="\n")
