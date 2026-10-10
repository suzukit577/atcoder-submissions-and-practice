N, M = map(int, input().split())
L, R = set(), set()
for _ in range(M):
    l, r = map(int, input().split())
    L.add(l)
    R.add(r)
print(max(min(R) - max(L) + 1, 0))
