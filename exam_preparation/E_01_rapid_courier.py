from collections import deque

packages = [int(x) for x in input().split()]
couriers = deque(int(x) for x in input().split())
total_delivered_weight = 0

while packages and couriers:
    current_package = packages.pop()
    current_courier = couriers.popleft()
    if current_courier >= current_package:
        if current_courier > current_package:
            current_courier -= 2 * current_package
            if current_courier > 0:
                couriers.append(current_courier)
        total_delivered_weight += current_package
    else:
        current_package -= current_courier
        packages.append(current_package)
        total_delivered_weight += current_courier

print(f"Total weight: {total_delivered_weight} kg")
if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(str(el) for el in packages)}")
elif not packages and couriers:
    print(f"Couriers are still on duty: {', '.join(str(el) for el in couriers)} but there are no more packages to deliver.")
