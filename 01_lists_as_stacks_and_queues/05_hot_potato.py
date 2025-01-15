from collections import deque

names = deque(input().split())
count_of_toss = int(input()) - 1

while len(names) > 1:
    names.rotate(-count_of_toss)
    name = names.popleft()
    print(f"Removed {name}")

print(f"Last is {names[0]}")
