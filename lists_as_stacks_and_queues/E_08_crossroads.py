from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
cars = deque()
cars_passed = 0
crash_happened = False
crashed_car = ""
character_hit = 0

command = input()
while command != "END":
    if command != "green":
        cars.append(command)
    else:
        remaining_green_light_time = green_light_duration
        while cars and remaining_green_light_time > 0:
            current_car = cars[0]
            current_car_length = len(current_car)
            if current_car_length <= remaining_green_light_time:
                remaining_green_light_time -= current_car_length
                cars_passed += 1
                cars.popleft()
            elif current_car_length <= remaining_green_light_time + free_window_duration:
                remaining_green_light_time -= current_car_length
                cars.popleft()
                cars_passed += 1
            else:
                character_hit = (current_car_length - remaining_green_light_time) - 1
                remaining_green_light_time = 0
                crashed_car = current_car
                crash_happened = True

        if crash_happened:
            break

    command = input()

if crash_happened:
    print("A crash happened!")
    print(f"{crashed_car} was hit at {crashed_car[character_hit]}.")
else:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")
