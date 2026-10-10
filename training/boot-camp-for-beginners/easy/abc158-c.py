import math

A, B = map(int, input().split())
ans = -1
for i in range(1, 10001):
    if math.floor(i * 0.08) == A and math.floor(i * 0.1) == B:
        ans = i
        break
print(ans)
