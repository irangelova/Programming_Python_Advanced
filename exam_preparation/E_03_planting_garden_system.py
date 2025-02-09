def plant_garden(available_garden_space, *allowed_plants, **planting_requests):
    planted_plant_types = {}
    allowed_plants_dict = {}
    requested_not_fully_executed = False
    for plant_type, space_required in allowed_plants:
        allowed_plants_dict[plant_type] = space_required
    #planting_requests_sorted = dict(sorted(planting_requests.items(), key=lambda x: x[0]))
    for requested_plant, requested_quantity in sorted(planting_requests.items()):
        if requested_plant in allowed_plants_dict.keys():
            if (requested_quantity * allowed_plants_dict[requested_plant]) <= available_garden_space:
                planted_plant_types[requested_plant] = int(requested_quantity)
                available_garden_space -= (requested_quantity * allowed_plants_dict[requested_plant])
            else:
                if int(available_garden_space // allowed_plants_dict[requested_plant]) == 0:
                    continue
                else:
                    planted_plant_types[requested_plant] = int(available_garden_space // allowed_plants_dict[requested_plant])
                    available_garden_space = 0

        if available_garden_space == 0 or not planting_requests:
            requested_not_fully_executed = True
            break

    result = []
    if not requested_not_fully_executed:
        result.append(f"All plants were planted! Available garden space: {available_garden_space:.1f} sq meters.")
    else:
        result.append("Not enough space to plant all requested plants!")
    planted_plant_types_sorted = sorted(planted_plant_types.items(), key=lambda x: x[0])
    result.append("Planted plants:")
    for plant, pieces in planted_plant_types_sorted:
        result.append(f"{plant}: {pieces}")

    return "\n".join(result)


print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))
