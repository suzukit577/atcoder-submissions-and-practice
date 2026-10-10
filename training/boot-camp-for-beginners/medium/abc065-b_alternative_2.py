# 別解 - 2
N = int(input())
a = [int(input()) - 1 for _ in range(N)]
res, cur = 0, 0
seen = [False for _ in range(N)]
while cur != 1:
    seen[cur] = True
    cur = a[cur]
    res += 1
    if seen[cur]:
        print(-1)
        exit()
print(res)
