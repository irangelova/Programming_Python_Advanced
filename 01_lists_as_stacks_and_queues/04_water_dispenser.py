from collections import deque

quantity_of_water = int(input())
people_needing_water = deque()

name = input()
while name != "Start":
    people_needing_water.append(name)
    name = input()

command = input()
while command != "End":
    if "refill" in command:
        _, liters_to_refill = command.split()
        quantity_of_water += int(liters_to_refill)
    else:
        liters_needed = int(command)
        if quantity_of_water >= liters_needed:
            print(f"{people_needing_water[0]} got water")
            people_needing_water.popleft()
            quantity_of_water -= liters_needed
        else:
            print(f"{people_needing_water[0]} must wait")
            people_needing_water.popleft()
    command = input()

print(f"{quantity_of_water} liters left")
