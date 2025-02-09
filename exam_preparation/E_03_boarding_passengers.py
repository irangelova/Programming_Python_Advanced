def boarding_passengers(capacity, *passenger_groups):
    boarding_information = {}
    passengers_not_boarded = 0
    passenger_groups_list = [el for el in passenger_groups]
    for group in passenger_groups:
        passenger_number, benefits_program = group
        if capacity >= int(passenger_number):
            if benefits_program not in boarding_information:
                boarding_information[benefits_program] = 0
            boarding_information[benefits_program] += int(passenger_number)
            capacity -= int(passenger_number)
            passenger_groups_list.remove(group)
        else:
            passengers_not_boarded += 1
            continue

        if capacity <= 0:
            if len(passenger_groups_list) > 0:
                passengers_not_boarded += len(passenger_groups_list)
            break

    boarding_information_sorted = sorted(boarding_information.items(), key=lambda x: (-x[1], x[0]))
    result = [f"Boarding details by benefit plan:"]
    for benefit_plan, number_of_passengers in boarding_information_sorted:
        result.append(f"## {benefit_plan}: {number_of_passengers} guests")
    if passengers_not_boarded == 0:
        result.append("All passengers are successfully boarded!")
    elif passengers_not_boarded > 0 and capacity == 0:
        result.append("Boarding unsuccessful. Cruise ship at full capacity.")
    elif capacity > 0 and passengers_not_boarded > 0:
        result.append(f"Partial boarding completed. Available capacity: {capacity}.")

    return "\n".join(result)


#print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
#print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
