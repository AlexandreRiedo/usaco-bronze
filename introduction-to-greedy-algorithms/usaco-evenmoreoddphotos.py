num_cows = int(input())
breed_ids = list(map(int, input().split()))
odd_count = sum(1 if id % 2 == 1 else 0 for id in breed_ids)
even_count = sum(1 if id % 2 == 0 else 0 for id in breed_ids)

group_number = 1
while True:
    if group_number % 2 == 0:
        if odd_count >= 1:
            group_number += 1
            odd_count -= 1
        else:
            break
    elif group_number % 2 == 1:
        if even_count >= 1:
            group_number += 1
            even_count -= 1
        elif odd_count >= 2:
            group_number += 1
            odd_count -= 2
        else:
            break

count = group_number - 1
if odd_count == 1:
    count -= 1
print(count)
