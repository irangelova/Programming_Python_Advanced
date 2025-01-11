from collections import deque

expression = input()
opening_parenthesis = []
closing_parenthesis = deque()
is_not_balanced = False

for character in expression:
    if character == "{" or character == "(" or character == "[":
        opening_parenthesis.append(character)
    else:
        closing_parenthesis.append(character)

for index in range(len(opening_parenthesis)):
    if len(opening_parenthesis) != len(closing_parenthesis):
        is_not_balanced = True
        break
    last_symbol = opening_parenthesis.pop()
    if last_symbol == "(" and closing_parenthesis.popleft() != ")":
        is_not_balanced = True
    elif last_symbol == "{" and closing_parenthesis.popleft() != "}":
        is_not_balanced = True
    elif last_symbol == "[" and closing_parenthesis.popleft() != "]":
        is_not_balanced = True

if is_not_balanced:
    print("NO")
else:
    print("YES")


