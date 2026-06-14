COWS = sorted(
    ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
)

cow_inds = {c: i for i, c in enumerate(COWS)}

neighbors = [[] for _ in range(len(COWS))]
with open("lineup.in") as read:
    for _ in range(int(read.readline())):
        words = read.readline().strip().split()

        # Convert the names to their index in the list
        cow1 = cow_inds[words[0]]
        cow2 = cow_inds[words[-1]]
        neighbors[cow1].append(cow2)
        neighbors[cow2].append(cow1)

order = []
added = [False for _ in range(len(COWS))]
for c in range(len(COWS)):
    if not added[c] and len(neighbors[c]) <= 1:
        added[c] = True
        order.append(c)

        if len(neighbors[c]) == 1:
            prev = c
            at = neighbors[c][0]
            
            while len(neighbors[at]) == 2:
                added[at] = True
                order.append(at)
                a, b = neighbors[at]
                at, prev = b if a == prev else a, at

            added[at] = True
            order.append(at)