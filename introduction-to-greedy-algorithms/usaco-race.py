import sys

sys.stdin = open("race.in")
sys.stdout = open("race.out", "w")


def dist_to_shift(curr_speed, target_speed):
    if curr_speed > target_speed:
        return sum(range(curr_speed - 1, target_speed - 1, -1))
    elif curr_speed < target_speed:
        return sum(range(curr_speed + 1, target_speed + 1))
    else:
        return 0


def shift_speed(pos, end_pos, speed, end_speed):
    dist_to_end = end_pos - pos

    if dist_to_end >= (speed + 1) + dist_to_shift(speed + 1, end_speed):
        return speed + 1
    if dist_to_end >= (speed) + dist_to_shift(speed, end_speed):
        return speed
    else:
        return speed - 1


def find_max_speed(end_pos):
    for max_speed in range(0, end_pos):
        if dist_to_shift(0, max_speed) >= end_pos:
            return max_speed

    return -666


length, num_cases = map(int, input().split())
max_speed = find_max_speed(length)
for _ in range(num_cases):
    target_speed = min(int(input()), max_speed)

    count = 0
    pos = 0
    speed = 0
    while pos < length:
        speed = shift_speed(pos, length, speed, target_speed)
        pos += speed
        count += 1

    print(f"{count}")
