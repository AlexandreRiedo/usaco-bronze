with open("taming.in") as f:
    N = int(f.readline())
    log = list(map(int, f.readline().split()))


def solve(log):
    m, M = 0, 0
    counter = -1  # -1 -> unset

    for idx in range(len(log) - 1, -1, -1):
        entry = log[idx]

        if counter != -1:
            counter -= 1

        if entry != -1 and counter != -1 and entry != counter:
            return ["-1"]

        if entry != -1:
            counter = entry

        if idx == 0:
            if entry > 0 or counter > 0:
                return ["-1"]
            m += 1
            M += 1
        else:
            if entry == -1:
                if counter == -1:
                    M += 1
                elif counter == 0:
                    m += 1
                    M += 1
            elif entry == counter == 0:
                m += 1
                M += 1

    return [str(m), str(M)]


with open("taming.out", "w") as f:
    f.write(f"{' '.join(solve(log))}\n")
