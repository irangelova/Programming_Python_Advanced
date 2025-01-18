from collections import deque

materials_box = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])
task_completed = False

toys = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

toys_produced = {}

while materials_box and magic_levels:
    current_material = materials_box[-1]
    current_magic = magic_levels[0]
    current_total_magic = current_material * current_magic
    if current_total_magic in toys:
        toy = toys[current_total_magic]
        if toy not in toys_produced:
            toys_produced[toy] = 0
        toys_produced[toy] += 1
        materials_box.pop()
        magic_levels.popleft()
    elif current_total_magic < 0:
        sum_magic = current_material + current_magic
        materials_box.pop()
        magic_levels.popleft()
        materials_box.append(sum_magic)
    elif current_total_magic > 0:
        magic_levels.popleft()
        materials_box[-1] += 15
    else:
        if current_material == 0 and current_magic == 0:
            materials_box.pop()
            magic_levels.popleft()
        elif current_material == 0:
            materials_box.pop()
        elif current_magic == 0:
            magic_levels.popleft()

if ("Doll" in toys_produced and "Wooden train" in toys_produced) or \
    ("Teddy bear" in toys_produced and "Bicycle" in toys_produced):
    task_completed = True

print(f"The presents are crafted! Merry Christmas!" if task_completed else "No presents this Christmas!")
if materials_box:
    print(f"Materials left: {', '.join(str(material) for material in reversed(materials_box))}")
if magic_levels:
    print(f"Magic left: {', '.join(str(magic) for magic in magic_levels)}")
for key, value in sorted(toys_produced.items()):
    print(f"{key}: {value}")
