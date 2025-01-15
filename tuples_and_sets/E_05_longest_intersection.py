#first_set = set()
#second_set = set()
longest_intersection = ""
longest_intersection_length = 0

for _ in range(int(input())):
    first_range, second_range = input().split("-")
    first_set = list(int(x) for x in first_range.split(","))
    second_set = list(int(x) for x in second_range.split(","))

    start_intersection = max(first_set[0], second_set[0])
    end_intersection = min(first_set[1], second_set[1])
    intersection = [start_intersection, end_intersection]
    current_length = 0
    current_intersection = []
    for number in range(start_intersection, end_intersection + 1):
        current_length += 1
        current_intersection.append(number)
    if current_length > longest_intersection_length:
        longest_intersection_length = current_length
        longest_intersection = current_intersection

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {longest_intersection_length}")
