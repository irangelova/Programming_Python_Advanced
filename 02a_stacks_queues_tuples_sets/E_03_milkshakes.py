from collections import deque

chocolates = [int(choc) for choc in input().split(", ")]
milk_cups = deque([int(cup) for cup in input().split(", ")])
milkshakes_made = 0

while chocolates and milk_cups and milkshakes_made < 5:
    current_choc = chocolates[-1]
    current_cup = milk_cups[0]
    if current_choc > 0 and current_cup > 0:
        if current_choc == current_cup:
            milkshakes_made += 1
            chocolates.pop()
            milk_cups.popleft()
        else:
            milk_cups.rotate(-1)
            chocolates[-1] -= 5
    elif current_choc <= 0 and current_cup <= 0:
        chocolates.pop()
        milk_cups.popleft()
    elif current_choc <= 0:
        chocolates.pop()
    else:
        milk_cups.popleft()

if milkshakes_made == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print(f"Chocolate: {', '.join(str(chocolate) for chocolate in chocolates)}" if chocolates else 'Chocolate: empty')
print(f"Milk: {', '.join(str(milk_cup) for milk_cup in milk_cups)}" if milk_cups else 'Milk: empty')
