num_points = int(input())
x_coords = [int(item) for item in input().split()]
y_coords = [int(item) for item in input().split()]

result = 0
for x, y in zip(x_coords, y_coords):
    for x_bis, y_bis in zip(x_coords, y_coords):
        result = max(result, abs(x - x_bis) ** 2 + abs(y - y_bis) ** 2)

print(result)
