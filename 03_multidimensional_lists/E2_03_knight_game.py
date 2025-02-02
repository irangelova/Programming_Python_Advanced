board_size = int(input())
knights_position = []
matrix = []
removed_knights = 0

for row in range(board_size):
    matrix.append([x for x in input()])
    for col in range(board_size):
        if matrix[row][col] == "K":
            knights_position.append([row, col])

possible_moves = [(-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2)]

while True:
    max_hits = 0
    max_knight = [0, 0]

    for k_row, k_col in knights_position:
        hits = 0
        for move in possible_moves:
            next_row = k_row + move[0]
            next_col = k_col + move[1]
            if 0 <= next_row < board_size and 0 <= next_col < board_size:
                if matrix[next_row][next_col] == "K":
                    hits += 1
        if hits > max_hits:
            max_hits = hits
            max_knight = [k_row, k_col]

    if max_hits == 0:
        break
    knights_position.remove(max_knight)
    matrix[max_knight[0]][max_knight[1]] = "0"
    removed_knights += 1

print(removed_knights)
