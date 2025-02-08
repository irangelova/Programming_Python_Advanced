from collections import deque
from math import ceil

bee_groups = deque(int(x) for x in input().split())
bee_eaters_group = [int(x) for x in input().split()]

while bee_groups and bee_eaters_group:
    current_bee_group = bee_groups.popleft()
    current_bee_eaters_group = bee_eaters_group[-1]
    if current_bee_group - (current_bee_eaters_group * 7) < 0: # Bee eaters won
        bee_eaters_group[-1] = ceil(((current_bee_eaters_group * 7) - current_bee_group) / 7)
    elif current_bee_group - (current_bee_eaters_group * 7) > 0: # Bees won
        bee_groups.append(current_bee_group - (current_bee_eaters_group * 7))
        bee_eaters_group.pop()
    else: # Bees = Bee eaters
        bee_eaters_group.pop()

print("The final battle is over!")
if not bee_groups and not bee_eaters_group:
    print("But no one made it out alive!")
if bee_groups:
    print(f"Bee groups left: {', '.join(str(el) for el in bee_groups)}")
if bee_eaters_group:
    print(f"Bee-eater groups left: {', '.join(str(el) for el in bee_eaters_group)}")
