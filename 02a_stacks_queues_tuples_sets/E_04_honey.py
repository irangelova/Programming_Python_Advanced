from collections import deque

bees = deque([int(x) for x in input().split()])
nectars = [int(x) for x in input().split()]
symbols = deque(x for x in input().split())
collected_honey = 0

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0
}

while bees and nectars:
    current_bee = bees[0]
    current_nectar = nectars.pop()
    if current_nectar >= current_bee:
        current_operation = symbols.popleft()
        collected_honey += abs(operations[current_operation](current_bee, current_nectar))
        bees.popleft()

print(f"Total honey made: {collected_honey}")
if bees:
    print(f"Bees left: {', '.join(str(bee) for bee in bees)}")
if nectars:
    print(f"Nectar left: {', '.join(str(nectar) for nectar in nectars)}")
