from collections import deque

pumps_number = int(input())
pumps = deque()

for _ in range(pumps_number):
    petrol, distance = input().split()
    pumps.append([int(petrol), int(distance)])

start_position = 0
stops = 0

while stops < pumps_number:
    fuel = 0
    for index in range(pumps_number):
        fuel += pumps[index][0]
        distance = pumps[index][1]
        if fuel < distance:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= distance
        stops += 1

print(start_position)
