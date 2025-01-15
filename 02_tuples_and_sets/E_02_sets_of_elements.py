first_set = set()
second_set = set()
first_length, second_length = map(int, input().split())

for _ in range(first_length):
    first_set.add(input())

#first_set = {input() for _ in range(first_length)}

for _ in range(second_length):
    second_set.add(input())

#second_set = {input() for _ in range(second_length)}

result = first_set.intersection(second_set)
print("\n".join(result))
