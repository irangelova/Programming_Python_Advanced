presents = int(input())
size = int(input())
matrix = []
santa_position = []
nice_kids = []
count_nice_kids = 0

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "S":
            santa_position = [row, col]
        elif matrix[row][col] == "V":
            nice_kids.append((row, col))

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
last_visited_house = []

while presents:
    command = input()
    if command == "Christmas morning":
        break
    else:
        direction = possible_moves[command]
        new_position_row = santa_position[0] + direction[0]
        new_position_col = santa_position[1] + direction[1]
        matrix[santa_position[0]][santa_position[1]] = "-"
        santa_position = [new_position_row, new_position_col]
        if 0 <= new_position_row < size and 0 <= new_position_col < size and matrix[new_position_row][new_position_col] != "-":
            if matrix[new_position_row][new_position_col] == "V":
                presents -= 1
                nice_kids.remove((santa_position[0], santa_position[1]))
                count_nice_kids += 1
            elif matrix[new_position_row][new_position_col] == "C":
                for direction, move in possible_moves.items():
                    row = santa_position[0] + move[0]
                    col = santa_position[1] + move[1]
                    if matrix[row][col] != "-":
                        presents -= 1
                    if matrix[row][col] == "V":
                        nice_kids.remove((row, col))
                        count_nice_kids += 1
                    matrix[row][col] = "-"
                    if presents <= 0:
                        break
        matrix[new_position_row][new_position_col] = "S"

if presents <= 0 and nice_kids:
    print("Santa ran out of presents!")
[print(*row) for row in matrix]
if not nice_kids:
    print(f"Good job, Santa! {count_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {len(nice_kids)} nice kid/s.")
