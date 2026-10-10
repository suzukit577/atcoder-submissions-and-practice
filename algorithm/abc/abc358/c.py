N, M = map(int, input().split())
S = [input() for _ in range(N)]
ans = N
for mask in range(1 << N):
    ok = [False] * M
    for i in range(N):
        if mask & (1 << i):
            for j in range(M):
                if S[i][j] == "o":
                    ok[j] = True
    if sum(ok) == M:
        ans = min(ans, bin(mask).count("1"))
print(ans)
