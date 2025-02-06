def age_assignment(*args, **kwargs):
    result = []
    [result.append(f"{name} is {kwargs[name[0]]} years old.") for name in sorted(args) if name[0] in kwargs.keys()]
    return "\n".join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))