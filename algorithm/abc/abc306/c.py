from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
dd = defaultdict(int)
ans = []
for a in A:
    dd[a] += 1
    if dd[a] == 2:
        ans.append(a)
print(*ans)
