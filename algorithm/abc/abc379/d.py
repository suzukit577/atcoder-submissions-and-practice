import bisect

Q = int(input())
plants = []
offset = 0
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        bisect.insort_right(plants, 0 - offset)
    elif query[0] == "2":
        T = int(query[1])
        offset += T
    elif query[0] == "3":
        H = int(query[1])
        idx = bisect.bisect_left(plants, H - offset)
        print(len(plants) - idx)
        plants = plants[:idx]
