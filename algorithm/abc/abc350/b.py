N, Q = map(int, input().split())
T = list(map(int, input().split()))
S = [True for _ in range(N)]
for t in T:
    if t <= 0 or N < t:
        pass
    elif S[t - 1] == True:
        S[t - 1] = False
    else:
        S[t - 1] = True
ans = 0
for s in S:
    if s == True:
        ans += 1
print(ans)
