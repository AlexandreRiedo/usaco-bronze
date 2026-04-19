num_flowers = int(input())
pedals = [int(item) for item in input().split()]

num_average_flower = 0
for i in range(num_flowers + 1):
    for j in range(i + 1, num_flowers + 1):
        if any(pedal == sum(pedals[i:j]) / (j - i) for pedal in pedals[i:j]):
            num_average_flower += 1
print(num_average_flower)
