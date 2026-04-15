import sys
from math import inf

sys.stdin = open("cbarn.in", "r")
sys.stdout = open("cbarn.out", "w")

num_rooms = int(input())
rooms = [int(input()) for _ in range(num_rooms)]


def solve(starting_index: int, rooms: list, num_rooms: int) -> int:
    res = 0
    index = (starting_index + 1) % num_rooms
    room_count = 1
    while index != ((starting_index) % num_rooms):
        res += (rooms[index] * room_count)
        index = (index+1) % num_rooms
        room_count += 1

    return res

min_distance = inf
for i in range(num_rooms):
    min_distance = min(min_distance, solve(i, rooms, num_rooms))
print(min_distance)