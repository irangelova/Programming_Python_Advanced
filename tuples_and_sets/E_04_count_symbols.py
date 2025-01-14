text = input()
occurrences = sorted(set(text))

for char in occurrences:
    print(f"{char}: {text.count(char)} time/s")
