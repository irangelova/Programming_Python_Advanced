def accommodate(*args, **kwargs):
    filled_rooms = {}
    unaccommodated_guests = 0
    kwargs = dict(sorted(kwargs.items(), key=lambda x: (x[1], x[0])))
    for guest_group in args:
        for room_key, capacity in kwargs.items():
            if capacity >= guest_group:
                room_number = room_key.split("_")[1]
                filled_rooms[room_number] = guest_group
                kwargs.pop(room_key)
                break
        else:
            unaccommodated_guests += guest_group

    if filled_rooms:
        result = [f"A total of {len(filled_rooms)} accommodations were completed!"]
        successful_accommodations_sorted = sorted(filled_rooms.items(), key=lambda x: x[0])
        for room, guests in successful_accommodations_sorted:
            result.append(f"<Room {room} accommodates {guests} guests>")
    else:
        result = ["No accommodations were completed!"]

    if unaccommodated_guests > 0:
        result.append(f"Guests with no accommodation: {unaccommodated_guests}")
    if kwargs:
        result.append(f"Empty rooms: {len(kwargs)}")

    return "\n".join(result)


print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
