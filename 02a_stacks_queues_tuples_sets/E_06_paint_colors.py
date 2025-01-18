from collections import deque

expression = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

collected_colors = []

while expression:
    first_substring = expression.popleft()
    last_substring = expression.pop() if expression else ""
    for checked_substring in (first_substring + last_substring, last_substring + first_substring):
        if checked_substring in main_colors or checked_substring in secondary_colors:
            collected_colors.append(checked_substring)
            break
    else:
        if len(first_substring) > 1:
            first_to_insert = first_substring[:-1]
            expression.insert((len(expression) // 2), first_to_insert)
        if len(last_substring) > 1:
            last_to_insert = last_substring[:-1]
            expression.insert((len(expression) // 2), last_to_insert)

for color in collected_colors:
    if color in secondary_colors:
        needed_colors = secondary_colors[color]
        for needed_color in needed_colors:
            if needed_color not in collected_colors:
                collected_colors.remove(color)
                break

print(collected_colors)

