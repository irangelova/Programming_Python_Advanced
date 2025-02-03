def sorting_cheeses(**kwargs):
    sorted_cheese = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ""
    for cheese, quantity in sorted_cheese:
        result += cheese + "\n"
        for el in sorted(quantity, reverse=True):
            result += f"{el}\n"
    return result



print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
