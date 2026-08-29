def convert(base10_num: int, base: int) -> int:
    ans = 0
    for idx, digit in enumerate(reversed(list(map(int, str(base10_num))))):
        ans += digit * (base**idx)
    return ans


with open("whatbase.in", "r") as fin, open("whatbase.out", "w") as fout:
    for _ in range(int(fin.readline())):
        num_X, num_Y = map(int, fin.readline().split())
        base_X, base_Y = 10, 10
        val_X, val_Y = convert(num_X, base_X), convert(num_Y, base_Y)

        while val_X != val_Y:
            if val_X < val_Y:
                base_X += 1
                val_X = convert(num_X, base_X)
            else:
                base_Y += 1
                val_Y = convert(num_Y, base_Y)

        fout.write(f"{base_X} {base_Y}\n")
