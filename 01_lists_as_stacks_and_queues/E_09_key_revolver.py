from collections import deque

price_of_bullet = int(input())
size_gun_barrel = int(input())
bullets = [int(bullet) for bullet in input().split()]
locks = deque(int(lock) for lock in input().split())
value_of_intelligence = int(input())
bullets_shot = 0

while bullets and locks:
    remaining_bullets = size_gun_barrel
    while remaining_bullets > 0 and bullets and locks:
        current_lock = locks[0]
        current_bullet = bullets.pop()
        bullets_shot += 1
        if current_lock >= current_bullet:
            locks.popleft()
            print("Bang!")
        else:
            print("Ping!")
        remaining_bullets -= 1
        if remaining_bullets == 0 and bullets:
            print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    money_earned = value_of_intelligence - (bullets_shot * price_of_bullet)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
