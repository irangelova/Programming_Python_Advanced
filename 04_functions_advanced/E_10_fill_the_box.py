def fill_the_box(*args):
    box_size = args[0] * args[1] * args[2]
    boxes = []
    for el in args[3:]:
        if el != "Finish":
            boxes.append(int(el))
        else:
            if box_size - sum(boxes) > 0:
                return f"There is free space in the box. You could put {box_size - sum(boxes)} more cubes."
            return f"No more free space! You have {abs(box_size - sum(boxes))} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
