def list_roman_emperors(*args, **kwargs):
    successful_emperors = {}
    unsuccessful_emperors = {}
    count_emperors = len(args)
    for name, status in args:
        if status:
            successful_emperors[name] = kwargs[name]
        else:
            unsuccessful_emperors[name] = kwargs[name]

    result = [f"Total number of emperors: {count_emperors}"]

    if successful_emperors:
        successful_emperors_sorted = sorted(successful_emperors.items(), key=lambda x: (-x[1], x[0]))
        result.append("Successful emperors:")
        for name, rule_years in successful_emperors_sorted:
            result.append(f"****{name}: {rule_years}")
    if unsuccessful_emperors:
        unsuccessful_emperors_sorted = sorted(unsuccessful_emperors.items(), key=lambda x: (x[1], x[0]))
        result.append("Unsuccessful emperors:")
        for name, rule_years in unsuccessful_emperors_sorted:
            result.append(f"****{name}: {rule_years}")

    return "\n".join(result)


print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))