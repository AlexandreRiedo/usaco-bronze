import math


def fastest_time(dist: int, max_speed: int):
    # We calculate the time it takes if only speeding up
    no_slow_time = int(math.ceil((math.sqrt(8 * dist + 1) - 1) / 2))
    if no_slow_time <= max_speed:
        return no_slow_time

    # Need to speed up past limit, so start at max speed for now
    speed_up_dist = max_speed * (max_speed - 1) // 2
    slow_down_dist = 0
    time = max_speed - 1

    curr_speed = max_speed
    while True:
        speed_up_dist += curr_speed
        time += 1
        if speed_up_dist + slow_down_dist >= dist:
            return time

        slow_down_dist += curr_speed
        time += 1
        if speed_up_dist + slow_down_dist >= dist:
            return time

        curr_speed += 1


with open("race.in") as read:
    dist, query_num = map(int, read.readline().split())

    with open("race.out", "w") as write:
        for _ in range(query_num):
            max_speed = int(read.readline())
            write.write(str(fastest_time(dist, max_speed)) + "\n")
