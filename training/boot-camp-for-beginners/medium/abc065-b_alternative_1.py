# 別解 - 1
N = int(input())
a = [int(input()) - 1 for _ in range(N)]
cur = 0
for i in range(N):
    cur = a[cur]
    if cur == 1:
        print(i + 1)
        exit()
print(-1)
