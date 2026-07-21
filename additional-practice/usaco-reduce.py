with open("reduce.in") as fin:
    N = int(fin.readline())
    locations = [tuple(map(int, fin.readline().split())) for _ in range(N)]

locations_x = list(sorted(locations, key=lambda x: x[0]))
locations_y = list(sorted(locations, key=lambda x: x[1]))

for _ in range(3):
    a, b, c, d = locations_x[0], locations_x[-1], locations_y[0], locations_y[-1]

    noa_a = locations_x[1]
    noa_b = b
    noa_c = c if c != a else locations_y[1]
    noa_d = d if d != a else locations_y[-2]
    noa_area = (noa_b[0] - noa_a[0]) * (noa_d[1] - noa_c[1])

    nob_b = locations_x[-2]
    nob_a = a
    nob_c = c if c != b else locations_y[1]
    nob_d = d if d != b else locations_y[-2]
    nob_area = (nob_b[0] - nob_a[0]) * (nob_d[1] - nob_c[1])

    noc_c = locations_y[1]
    noc_a = a if a != c else locations_x[1]
    noc_b = b if b != c else locations_x[-2]
    noc_d = d
    noc_area = (noc_b[0] - noc_a[0]) * (noc_d[1] - noc_c[1])

    nod_d = locations_y[-2]
    nod_a = a if a != d else locations_x[1]
    nod_b = b if b != d else locations_x[-2]
    nod_c = c
    nod_area = (nod_b[0] - nod_a[0]) * (nod_d[1] - nod_c[1])

    if min(noa_area, nob_area, noc_area, nod_area) == noa_area:
        locations_x.remove(a)
        locations_y.remove(a)
    elif min(noa_area, nob_area, noc_area, nod_area) == nob_area:
        locations_x.remove(b)
        locations_y.remove(b)
    elif min(noa_area, nob_area, noc_area, nod_area) == noc_area:
        locations_x.remove(c)
        locations_y.remove(c)
    elif min(noa_area, nob_area, noc_area, nod_area) == nod_area:
        locations_x.remove(d)
        locations_y.remove(d)

with open("reduce.out", "w") as fout:
    a, b, c, d = locations_x[0], locations_x[-1], locations_y[0], locations_y[-1]
    ans = (b[0] - a[0]) * (d[1] - c[1])
    fout.write(f"{ans}\n")


"""
7
-5 25
-3 9
-1 1
0 0
2 4
4 16
6 36
"""

"""
6
1 1
7 8
10 9
8 12
4 100
50 7
"""
