expression = input()

opening_parenthesis = "([{"
closing_parenthesis = ")]}"
parenthesis = []
is_balanced = True

for character in expression:
    if character in opening_parenthesis:
        parenthesis.append(character)
    elif character in closing_parenthesis:
        if not parenthesis:
            is_balanced = False
            break
        last_parenthesis = parenthesis.pop()
        if opening_parenthesis.index(last_parenthesis) != closing_parenthesis.index(character):
            is_balanced = False
            break
else:
    if parenthesis:
        is_balanced = False

if is_balanced:
    print("YES")
else:
    print("NO")