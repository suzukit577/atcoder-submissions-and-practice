N = int(input())
a = [int(input()) - 1 for _ in range(N)]
cur, cnt, visited = 0, 0, set()
for _ in range(N):
    if a[cur] == 1:
        break
    if a[cur] in visited:
        print(-1)
        exit()
    visited.add(cur)
    cur = a[cur]
    cnt += 1
print(cnt + 1)
