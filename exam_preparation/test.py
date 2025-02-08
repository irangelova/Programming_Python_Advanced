dictionary = {"1": 2, "2": 4}
group_number = 5

for key, value in dictionary.items():
    if group_number == value:
        print(f"matched numbers, room {key}")
        break
    elif value > group_number:
        print(f"not exact match, room {key}")
        break
else:
    print("no match, currently no room available")

