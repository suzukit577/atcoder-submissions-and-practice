# 別解
import bisect

N, M, D = map(int, input().split())
A = sorted(map(int, input().split()))
B = list(map(int, input().split()))
ans = -1
for b in B:
    i = bisect.bisect_right(A, b + D) - 1
    if i >= 0 and A[i] >= b - D:
        ans = max(ans, A[i] + b)
print(ans)
