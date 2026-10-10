N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]
ans = 0
for i in range(N):
    cnt = sum(A[0][: i + 1] + A[1][i:])
    ans = max(ans, cnt)
print(ans)
