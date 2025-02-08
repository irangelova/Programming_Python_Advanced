def list_roman_emperors(*args, **kwargs):
    successful_emperors = {}
    unsuccessful_emperors = {}
    count_emperors = len(args)
    for rule_status in args:
        if rule_status[1]:
            successful_emperors[rule_status[0]] = 0
        else:
            unsuccessful_emperors[rule_status[0]] = 0

    for name, rule_length in kwargs.items():
        if name in successful_emperors.keys():
            successful_emperors[name] = int(rule_length)
        else:
            unsuccessful_emperors[name] = int(rule_length)

    successful_emperors_res = dict(sorted(successful_emperors.items(), key=lambda x: (-x[1], x[0])))
    unsuccessful_emperors_res = dict(sorted(unsuccessful_emperors.items(), key=lambda x: (x[1], x[0])))
    count_emperors_output = f"Total number of emperors: {count_emperors}"
    successful_emperors_str = successful_emperors_output = unsuccessful_emperors_str = unsuccessful_emperors_output = ""
    if successful_emperors:
        successful_emperors_str = "Successful emperors:"
        successful_emperors_output = '\n'.join(f"****{name}: {rule_years}" for name, rule_years in successful_emperors_res.items())
    if unsuccessful_emperors:
        unsuccessful_emperors_str = "Unsuccessful emperors:"
        unsuccessful_emperors_output = '\n'.join(f"****{name_u}: {rule_years_u}" for name_u, rule_years_u in unsuccessful_emperors_res.items())
    return f"{count_emperors_output}\n{successful_emperors_str}\n{successful_emperors_output}\n{unsuccessful_emperors_str}\n{unsuccessful_emperors_output}"


print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))