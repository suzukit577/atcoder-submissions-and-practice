N, C = map(int, input().split())
T = list(map(int, input().split()))
ans, time = 0, 0
for i in range(N):
    if i == 0:
        ans += 1
        time = T[i]
    else:
        if T[i] - time >= C:
            ans += 1
            time = T[i]
print(ans)
