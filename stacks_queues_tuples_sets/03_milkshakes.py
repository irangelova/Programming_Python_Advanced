#first_set = set()
#second_set = set()
longest_intersection = set()
longest_intersection_length = 0

for _ in range(int(input())):
    first_range, second_range = input().split("-")
    first_set = set(int(x) for x in first_range.split(","))
    second_set = set(int(x) for x in second_range.split(","))

    intersection = first_set.intersection(second_set)
    if len(intersection) > longest_intersection_length:
        longest_intersection_length = len(intersection)
        longest_intersection.add(intersection)

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {longest_intersection_length}")
