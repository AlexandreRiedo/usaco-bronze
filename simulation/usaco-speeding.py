import sys

ROAD_SIZE = 100

sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")

num_road_segments, num_bessie_segments = map(int, input().split())
road_segments = []
for _ in range(num_road_segments):
    road_segments.append(tuple(map(int, input().split())))
bessie_segments = []
for _ in range(num_bessie_segments):
    bessie_segments.append(tuple(map(int, input().split())))

road_speeds = []
for road_segment in road_segments:
    for _ in range(road_segment[0]):
        road_speeds.append(road_segment[1])
bessie_speeds = []
for bessie_segment in bessie_segments:
    for _ in range(bessie_segment[0]):
        bessie_speeds.append(bessie_segment[1])

max_speeding = 0
for road_speed, bessie_speed in zip(road_speeds, bessie_speeds):
    max_speeding = max(max_speeding, max(0, bessie_speed - road_speed))
print(max_speeding)
