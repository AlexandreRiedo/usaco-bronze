CALENDAR_IDX = {
    "Ox": 0,
    "Tiger": 1,
    "Rabbit": 2,
    "Dragon": 3,
    "Snake": 4,
    "Horse": 5,
    "Goat": 6,
    "Monkey": 7,
    "Rooster": 8,
    "Dog": 9,
    "Pig": 10,
    "Rat": 11,
}

CALENDAR = [
    "Ox",
    "Tiger",
    "Rabbit",
    "Dragon",
    "Snake",
    "Horse",
    "Goat",
    "Monkey",
    "Rooster",
    "Dog",
    "Pig",
    "Rat",
]


num_lines = int(input())
cows = {"Bessie": (0, "Ox")}
for _ in range(num_lines):
    cow_a, _, _, direction, cow_a_animal, _, _, cow_b = input().split()

    cow_b_year, cow_b_animal = cows[cow_b]

    if direction == "previous":
        if cow_a_animal == cow_b_animal:
            cows[cow_a] = (cow_b_year - 12, cow_a_animal)
        else:
            count = 1
            start_idx = CALENDAR_IDX[cow_b_animal] - 1
            while CALENDAR[start_idx] != cow_a_animal:
                count += 1
                start_idx -= 1
            cows[cow_a] = (cow_b_year - count, cow_a_animal)
    elif direction == "next":
        if cow_a_animal == cow_b_animal:
            cows[cow_a] = (cow_b_year + 12, cow_a_animal)
        else:
            count = 1
            start_idx = (CALENDAR_IDX[cow_b_animal] + 1) % len(CALENDAR)
            while CALENDAR[start_idx] != cow_a_animal:
                count += 1
                start_idx = (start_idx + 1) % len(CALENDAR)
            cows[cow_a] = (cow_b_year + count, cow_a_animal)

print(abs(cows["Elsie"][0]))
