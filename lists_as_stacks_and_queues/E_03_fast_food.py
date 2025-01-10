from collections import deque

quantity_of_food = int(input())
food_in_each_order = input().split()
food_per_order = deque()

for index in range(len(food_in_each_order)):
    food_per_order.append(int(food_in_each_order[index]))

biggest_order = max(food_per_order)
print(biggest_order)
while food_per_order:
    current_order = food_per_order[0]
    if current_order <= quantity_of_food:
        quantity_of_food -= food_per_order.popleft()
    else:
        break

if not food_per_order:
    print("Orders complete")
else:
    print(f"Orders left:", *food_per_order)
