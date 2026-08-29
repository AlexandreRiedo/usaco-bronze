def convert(base10_num: int, base: int) -> int:
    ans = 0
    for idx, digit in enumerate(reversed(list(map(int, str(base10_num))))):
        ans += digit * (base**idx)
    return ans


with open("whatbase.in", "r") as fin, open("whatbase.out", "w") as fout:
    for _ in range(int(fin.readline())):
        in_num_X, in_num_Y = map(int, fin.readline().split())
        num_X, num_Y = min(in_num_X, in_num_Y), max(in_num_X, in_num_Y)

        base_X, base_Y = 10, 10
        new_X, new_Y = convert(num_X, base_X), convert(num_Y, base_Y)
        while new_X != new_Y:
            if new_X < new_Y:
                base_X += 1
            else:
                base_Y += 1
            new_X, new_Y = convert(num_X, base_X), convert(num_Y, base_Y)

        if num_X == in_num_X:
            fout.write(f"{base_X} {base_Y}\n")
        else:
            fout.write(f"{base_Y} {base_X}\n")
