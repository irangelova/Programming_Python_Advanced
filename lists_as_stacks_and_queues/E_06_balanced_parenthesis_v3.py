from collections import deque

expression = input()
parenthesis = {"(": ")", "[": "]", "{": "}"}

opening_parenthesis = []
closing_parenthesis = deque()
is_balanced = False

for character in expression:
    if character in parenthesis.keys():
        opening_parenthesis.append(character)
    else:
        if not opening_parenthesis:
            is_balanced = False
            break
        closing_parenthesis.append(character)

for index in range(len(opening_parenthesis)):
    if len(opening_parenthesis) != len(closing_parenthesis):
        is_balanced = False
        break
    last_opening_symbol = opening_parenthesis.pop()
    first_closing_symbol = closing_parenthesis.popleft()
    if parenthesis[last_opening_symbol] != first_closing_symbol:
        is_balanced = False
        break

if is_balanced:
    print("YES")
else:
    print("NO")
