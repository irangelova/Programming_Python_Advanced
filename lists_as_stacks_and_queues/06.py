from collections import deque

expression = input()
parenthesis = {"(": ")", "[": "]", "{": "}"}

opening_parenthesis = []
closing_parenthesis = deque()
is_balanced = True  # Start with True instead of False

for character in expression:
    if character in parenthesis.keys():
        opening_parenthesis.append(character)
    else:
        if not opening_parenthesis:  # If we get a closing bracket with no opening bracket
            is_balanced = False
            break
        # Check if current closing bracket matches the last opening bracket
        last_opening = opening_parenthesis.pop()
        if parenthesis[last_opening] != character:  # Compare directly with current character
            is_balanced = False
            break

# Check if we have any remaining opening brackets
if opening_parenthesis and is_balanced:  # If there are unclosed brackets
    is_balanced = False

print("YES" if is_balanced else "NO")