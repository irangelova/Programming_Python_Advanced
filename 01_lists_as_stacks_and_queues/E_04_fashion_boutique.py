clothes_in_box = [int(element) for element in input().split()]
capacity_of_rack = int(input())
capacity_needed = 0
racks_needed = 1

while clothes_in_box:
    current_clothes = clothes_in_box[-1]
    capacity_needed += current_clothes
    if capacity_needed <= capacity_of_rack:
        clothes_in_box.pop()
    else:
        racks_needed += 1
        capacity_needed = 0

print(racks_needed)
