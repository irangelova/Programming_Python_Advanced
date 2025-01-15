number_of_guests = int(input())
reservations = set()

for _ in range(number_of_guests):
    reservation_code = input()
    reservations.add(reservation_code)

reservation_came = input()
while reservation_came != "END":
    if reservation_came in reservations:
        reservations.remove(reservation_came)
    reservation_came = input()

print(len(reservations))
print("\n".join(sorted(reservations)))
