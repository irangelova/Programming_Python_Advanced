from collections import deque

cups = deque(int(cup) for cup in input().split())
filled_bottles = [int(bottle) for bottle in input().split()]
wasted_water = 0

while cups and filled_bottles:
    current_cup = cups[0]
    while current_cup > 0:
        current_bottle = filled_bottles.pop()
        if current_cup >= current_bottle:
            current_cup -= current_bottle
            if current_cup == 0:
                cups.popleft()
        else:
            wasted_water += current_bottle - current_cup
            current_cup = 0
            cups.popleft()

if not cups:
    print(f"Bottles: {' '.join([str(element) for element in filled_bottles])}")
elif not filled_bottles:
    print(f"Cups: {' '.join([str(element) for element in cups])}")
print(f"Wasted litters of water: {wasted_water}")

