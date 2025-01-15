numbers = tuple(float(element) for element in input().split())

occurrences = {}
for number in numbers:
    occurrences[number] = numbers.count(number)

for key, value in occurrences.items():
    print(f"{key} - {value} times")
