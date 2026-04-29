import sys

sys.setrecursionlimit(1_000_000)
res = []
ele = []


def backtrack():
    if len(ele) == 0:
        print(" ".join([str(num) for num in res]))
        exit()

    for i in range(len(ele) - 1, -1, -1):
        x = ele[i]

        if len(res) == 0 or abs(res[-1] - x) != 1:
            del ele[i]
            res.append(x)
            backtrack()
            res.pop()
            ele.insert(i, x)


def main():
    n = int(input())

    if n == 2 or n == 3:
        print("NO SOLUTION")
        return

    for i in range(n, 0, -1):
        ele.append(i)

    backtrack()


if __name__ == "__main__":
    main()
