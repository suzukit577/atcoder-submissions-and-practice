N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
ans, j = 0, 0
for b in B:
    while j < N and A[j] < b:
        j += 1
    if j == N:
        print(-1)
        break
    ans += A[j]
    j += 1
else:
    print(ans)
