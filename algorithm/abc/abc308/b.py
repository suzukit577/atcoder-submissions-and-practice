N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))
ans = 0
price = dict()
for i in range(M):
    price[D[i]] = P[i + 1]
for c in C:
    if c in D:
        ans += price[c]
    else:
        ans += P[0]
print(ans)
