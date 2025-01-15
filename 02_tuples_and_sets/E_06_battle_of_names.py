even_set = set()
odd_set = set()

for row in range(1, int(input()) + 1):
    current_name_sum = 0
    current_name = input()
    #for char in current_name:
    #    current_name_sum += ord(char)
    #current_name_sum //= rows
    current_name_sum += sum(ord(char) for char in current_name) // row
    if current_name_sum % 2 == 0:
        even_set.add(current_name_sum)
    else:
        odd_set.add(current_name_sum)

sum_even_set = sum(even_set)
sum_odd_set = sum(odd_set)

if sum_even_set == sum_odd_set:
    print(", ".join(str(x) for x in even_set.union(odd_set)))
elif sum_odd_set > sum_even_set:
    print(", ".join(str(x) for x in odd_set.difference(even_set)))
else:
    print(", ".join(str(x) for x in even_set.symmetric_difference(odd_set)))
