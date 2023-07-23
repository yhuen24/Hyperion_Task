# pylint: disable-all
# 100 doors challenge
doors = []
for _ in range(0, 101):
    doors.append(False)

for step in range(1, 101):
    for door in range(1, 101):
        if door % step == 0:
            doors[door] = not doors[door]

for i in range(1, 101):
    if doors[i]:
        print(i)
