from collections import deque


def process_traffic():
    # Get initial durations
    green_duration = int(input())
    free_window = int(input())

    cars_queue = deque()
    total_cars_passed = 0

    while True:
        command = input()

        if command == "END":
            print("Everyone is safe.")
            print(f"{total_cars_passed} total cars passed the crossroads.")
            break

        if command == "green":
            # Process cars during green light
            current_green = green_duration

            # Process cars while there's still green light time
            while current_green > 0 and cars_queue:
                current_car = cars_queue.popleft()

                # If car can pass completely in green light
                if len(current_car) <= current_green:
                    current_green -= len(current_car)
                    total_cars_passed += 1
                    continue

                # If car is partially in intersection
                remaining_car = len(current_car) - current_green

                # Check if car can pass during free window
                if remaining_car <= free_window:
                    total_cars_passed += 1
                else:
                    # Crash occurs - car couldn't pass in time
                    hit_index = current_green + free_window
                    print("A crash happened!")
                    print(f"{current_car} was hit at {current_car[hit_index]}.")
                    return

                # Break after processing partial car
                break

        else:
            # Add new car to queue
            cars_queue.append(command)


# Run the traffic system
process_traffic()