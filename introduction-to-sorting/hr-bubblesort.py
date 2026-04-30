#!/bin/python3


#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#


def countSwaps(a):
    num_swaps = 0

    for i in range(0, n):
        for j in range(0, n - 1):
            if a[j] > a[j + 1]:
                num_swaps += 1
                a[j], a[j + 1] = a[j + 1], a[j]

    print(f"Array is sorted in {num_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


if __name__ == "__main__":
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
