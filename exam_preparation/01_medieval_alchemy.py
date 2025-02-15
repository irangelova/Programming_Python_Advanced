from collections import deque

substances = [int(x) for x in input().split(", ")]
crystals = deque(int(x) for x in input().split(", "))

potions = {
    110: "Brew of Immortality",
    100: "Essence of Resilience",
    90: "Draught of Wisdom",
    80:  "Potion of Agility",
    70: "Elixir of Strength"
}

potions_made = 0
potions_made_names = []

while potions_made < 5 and substances and crystals:
    current_substance = substances.pop()
    current_crystal = crystals.popleft()
    current_sum = current_substance + current_crystal
    if current_sum in potions.keys() and potions[current_sum] not in potions_made_names:
        potions_made += 1
        potions_made_names.append(potions[current_sum])
    else:
        for energy, potion in potions.items():
            if energy < current_sum and potion not in potions_made_names:
                potions_made += 1
                potions_made_names.append(potion)
                if current_crystal > 20:
                    crystals.append(current_crystal - 20)
                break
        else:
            if current_crystal > 5:
                crystals.append(current_crystal - 5)

if potions_made == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")
if potions_made_names:
    print(f"Crafted potions: {', '.join(potions_made_names)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in reversed(substances))}")
if crystals:
    print(f"Crystals: {', '.join(str(x) for x in crystals)}")
