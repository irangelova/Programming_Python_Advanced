unique_elements = set()

for _ in range(int(input())):
    elements = input().split()
    for element in elements:
        unique_elements.add(element)

print("\n".join(unique_elements))
