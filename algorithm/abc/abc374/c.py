N = int(input())
K = list(map(int, input().split()))
ans, min_diff = 0, 10**10
for mask in range(1 << N):
    A, B = 0, 0
    for i in range(N):
        if mask & (1 << i):
            A += K[i]
        else:
            B += K[i]
    diff = abs(A - B)
    if diff < min_diff:
        min_diff = diff
        ans = max(A, B)
print(ans)
