from collections import defaultdict
from functools import reduce
from typing import NamedTuple


class DrinkLog(NamedTuple):
    milk_type: int
    time: int


with open("badmilk.in") as file:
    num_friends, num_milks, num_drinks, num_sicks = map(int, file.readline().split())

    drink_logs = {friend: [] for friend in range(1, num_friends + 1)}
    persons_per_milk = defaultdict(set)
    for _ in range(num_drinks):
        person, milk_type, time = map(int, file.readline().split())
        drink_logs[person].append(DrinkLog(milk_type, time))
        persons_per_milk[milk_type].add(person)

    sick_logs = defaultdict(int)
    sick_friends = set()
    for _ in range(num_sicks):
        person, time = map(int, file.readline().split())
        sick_logs[person] = time
        sick_friends.add(person)

# rprint("")
# rprint(f"{drink_logs=}")
# rprint(f"{sick_logs=}")
# rprint(f"{persons_per_milk=}")
# rprint("")

potentially_bad_milks_per_friend = {sick_friend: set() for sick_friend in sick_friends}
for person, drinking_history in filter(
    lambda kv: kv[0] in sick_friends, drink_logs.items()
):
    last_sick_time = sick_logs[person]

    for drink_log in drinking_history:
        if drink_log.time < last_sick_time:
            potentially_bad_milks_per_friend[person].add(drink_log.milk_type)

    # rprint(f"{person=}")
    # rprint(f"{last_sick_time=}")
# rprint("")
# rprint(f"{potentially_bad_milks_per_friend=}")

potentially_bad_milks = set(
    reduce(lambda a, b: a.intersection(b), potentially_bad_milks_per_friend.values())
)
# rprint("")
# rprint(f"{potentially_bad_milks=}")

max_potential_sickness = max(
    len(persons_per_milk[milk_type]) for milk_type in potentially_bad_milks
)
# rprint(f"{max_potential_sickness=}")

with open("badmilk.out", "w") as file:
    file.write(f"{max_potential_sickness}\n")
