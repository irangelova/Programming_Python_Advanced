from collections import deque

strength = [int(x) for x in input().split()]
accuracy = deque(input().split())
count_goals = 0

while strength and accuracy:
    current_sum = strength[-1] + int(accuracy[0])
    if current_sum == 100:
        strength.pop()
        accuracy.popleft()
        count_goals += 1
    elif current_sum < 100:
        if strength[-1] < int(accuracy[0]):
            strength.pop()
        elif strength[-1] > int(accuracy[0]):
            accuracy.popleft()
        elif strength[-1] == int(accuracy[0]):
            strength.pop()
            strength.append(current_sum)
            accuracy.popleft()
    elif current_sum > 100:
        last_el_strength = strength[-1] - 10
        strength.pop()
        strength.append(last_el_strength)
        accuracy.rotate(-1)

if count_goals == 3:
    print("Paul scored a hat-trick!")
if count_goals == 0:
    print("Paul failed to score a single goal.")
if count_goals > 3:
    print("Paul performed remarkably well!")
if 0 < count_goals < 3:
    print("Paul failed to make a hat-trick.")
if count_goals > 0:
    print(f"Goals scored: {count_goals}")
if strength:
    print(f"Strength values left: {', '.join(str(el) for el in strength)}")
if accuracy:
    print(f"Accuracy values left: {', '.join(accuracy)}")
