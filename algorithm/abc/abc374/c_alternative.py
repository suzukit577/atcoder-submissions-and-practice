# 別解
N = int(input())
K = list(map(int, input().split()))
ans = 10**10
for mask in range(1 << N):
    A, B = 0, 0
    for i in range(N):
        if mask & (1 << i):
            A += K[i]
        else:
            B += K[i]
    ans = min(ans, max(A, B))
print(ans)
