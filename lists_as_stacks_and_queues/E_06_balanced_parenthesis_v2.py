from collections import deque

expression = input()
parenthesis = {"(": ")", "[": "]", "{": "}"}

opening_parenthesis = []
is_balanced = True

for character in expression:
    if character in parenthesis.keys():
        opening_parenthesis.append(character)
    else:
        if not opening_parenthesis:
            is_balanced = False
            break
        last_opening_symbol = opening_parenthesis.pop()
        if parenthesis[last_opening_symbol] != character:
            is_balanced = False
            break

if opening_parenthesis and is_balanced:
    is_balanced = False

if is_balanced:
    print("YES")
else:
    print("NO")
