size = int(input())
matrix = []
alice_position = []

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "A":
            matrix[row][col] = "*"
            alice_position = [row, col]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}


bags_collected = 0

while bags_collected < 10:
    command = input()
    moves = possible_moves[command]
    new_position_row = moves[0] + alice_position[0]
    new_position_col = moves[1] + alice_position[1]
    if new_position_row < 0 or new_position_row > (size - 1) or new_position_col < 0 or new_position_col > (size - 1):
        print("Alice didn't make it to the tea party.")
        break
    if matrix[new_position_row][new_position_col] == "R":
        matrix[new_position_row][new_position_col] = "*"
        print("Alice didn't make it to the tea party.")
        break
    if matrix[new_position_row][new_position_col] != "." and matrix[new_position_row][new_position_col] != "*":
        bags_collected += int(matrix[new_position_row][new_position_col])
    matrix[new_position_row][new_position_col] = "*"
    alice_position = [new_position_row, new_position_col]

if bags_collected >= 10:
    print("She did it! She went to the party.")
# for row in matrix:
#     print(*row, sep=" ")

[print(*row) for row in matrix]