from collections import deque

amount_of_money = [int(x) for x in input().split()]
food_prices = deque(int(x) for x in input().split())
food_eaten = 0

while amount_of_money and food_prices:
    current_amount = amount_of_money.pop()
    current_price = food_prices.popleft()
    if current_amount == current_price:
        food_eaten += 1
    if current_amount > current_price:
        food_eaten += 1
        change = current_amount - current_price
        if amount_of_money:
            amount_of_money[-1] += change


if food_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {food_eaten} foods.")
elif 1 < food_eaten < 4:
    print(f"Henry ate: {food_eaten} foods.")
elif food_eaten == 1:
    print(f"Henry ate: {food_eaten} food.")
else:
    print("Henry remained hungry. He will try next weekend again.")
