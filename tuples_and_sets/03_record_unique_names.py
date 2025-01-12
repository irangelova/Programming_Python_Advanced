count_of_names = int(input())
unique_name = set()

for _ in range(count_of_names):
    name = input()
    unique_name.add(name)

print("\n".join(unique_name))
